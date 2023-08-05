use eframe::egui::*;

use serde::{Deserialize, Serialize};
use std::borrow::Cow;

use newsapi::NewsApi;

pub const PADDING: f32 = 5.0;
const WHITE: Color32 = Color32::from_rgb(255, 255, 255);
const BLACK: Color32 = Color32::from_rgb(0, 0, 0);
const CYAN: Color32 = Color32::from_rgb(0, 255, 255);
const RED: Color32 = Color32::from_rgb(255, 0, 0);

pub enum Msg {
    ApiKeySet(String),
}

#[derive(Serialize, Deserialize)]
pub struct HeadlinesConfig {
    pub dark_mode: bool,
    pub api_key: String,
}

impl Default for HeadlinesConfig {
    fn default() -> Self {
        Self {
            dark_mode: true,
            api_key: String::new(),
        }
    }
}

pub struct Headlines {
    pub articles: Vec<NewsCardData>,
    pub config: HeadlinesConfig,
    pub api_key_initialized: bool,
    pub news_rx: Option<std::sync::mpsc::Receiver<NewsCardData>>,
    pub app_tx: Option<std::sync::mpsc::SyncSender<Msg>>,
}

impl Headlines {
    pub fn new() -> Headlines {
        let config: HeadlinesConfig = confy::load("headlines", "headlines").unwrap_or_default();

        Headlines {
            articles: Vec::new(),
            api_key_initialized: !config.api_key.is_empty(),
            news_rx: None,
            app_tx: None,
            config,
        }
    }

    pub fn configure_fonts(&self, ctx: &eframe::egui::CtxRef) {
        let mut font_def = FontDefinitions::default();
        font_def.font_data.insert(
            "MesloLGS".to_string(),
            Cow::Borrowed(include_bytes!("../../MesloLGS_NF_Regular.ttf")),
        );
        font_def
            .family_and_size
            .insert(TextStyle::Heading, (FontFamily::Proportional, 35.));
        font_def
            .family_and_size
            .insert(TextStyle::Body, (FontFamily::Proportional, 20.));

        font_def
            .fonts_for_family
            .get_mut(&FontFamily::Proportional)
            .unwrap()
            .insert(0, "MesloLGS".to_string());

        ctx.set_fonts(font_def);
    }

    pub fn render_news_cards(&self, ui: &mut Ui) {
        for a in &self.articles {
            ui.add_space(PADDING);
            // render title
            let title = format!("▶ {}", a.title);
            if self.config.dark_mode {
                ui.colored_label(WHITE, title);
            } else {
                ui.colored_label(BLACK, title);
            }

            // render desc
            ui.add_space(PADDING);
            let desc = Label::new(&a.desc).text_style(TextStyle::Button);
            ui.add(desc);

            // render hyperlinks
            if self.config.dark_mode {
                ui.style_mut().visuals.hyperlink_color = CYAN;
            } else {
                ui.style_mut().visuals.hyperlink_color = RED;
            }
            ui.add_space(PADDING);
            ui.with_layout(Layout::right_to_left(), |ui| {
                ui.add(Hyperlink::new(&a.url).text("read more ⤴"));
            });
            ui.add_space(PADDING);
            ui.add(Separator::default());
        }
    }

    pub fn render_top_panel(&mut self, ctx: &CtxRef, frame: &mut eframe::epi::Frame<'_>) {
        // define a TopBottomPanel widget
        TopBottomPanel::top("top_panel").show(ctx, |ui| {
            ui.add_space(10.);
            menu::bar(ui, |ui| {
                // logo
                ui.with_layout(Layout::left_to_right(), |ui| {
                    ui.add(Label::new("📓").text_style(TextStyle::Heading));
                });
                // controls
                ui.with_layout(Layout::right_to_left(), |ui| {
                    let close_btn = ui.add(Button::new("❌").text_style(TextStyle::Body));
                    if close_btn.clicked() {
                        frame.quit();
                    }

                    let refresh_btn = ui.add(Button::new("🔄").text_style(TextStyle::Body));
                    if refresh_btn.clicked() {
                        self.load_news()
                    }

                    let theme_btn = ui.add(
                        Button::new(if self.config.dark_mode {
                            "🌞"
                        } else {
                            "🌙"
                        })
                        .text_style(TextStyle::Body),
                    );
                    if theme_btn.clicked() {
                        self.config.dark_mode = !self.config.dark_mode;
                    }
                });
            });
            ui.add_space(10.);
        });
    }

    pub fn preload_articles(&mut self) {
        if let Some(rx) = &self.news_rx {
            match rx.try_recv() {
                Ok(x) => self.articles.push(x),
                Err(_) => {}
            }
        }
    }

    pub fn render_config(&mut self, ctx: &CtxRef) {
        Window::new("Configuration").show(ctx, |ui| {
            ui.label("Entry");
            let text_input = ui.text_edit_singleline(&mut self.config.api_key);
            if text_input.lost_focus() && ui.input().key_pressed(Key::Enter) {
                if let Err(e) = confy::store(
                    "headlines",
                    "headlines",
                    HeadlinesConfig {
                        dark_mode: self.config.dark_mode,
                        api_key: self.config.api_key.to_string(),
                    },
                ) {
                    tracing::error!("Failed saving app state: {}", e);
                }
                self.api_key_initialized = true;
                if let Some(tx) = &self.app_tx {
                    tx.send(Msg::ApiKeySet(self.config.api_key.to_string()))
                        .unwrap_or_else(|e| tracing::error!("Cannot send Msg::ApiKeySet, {}", e));
                }
            }
            ui.label("If you haven't registered for the API_KEY, head over to");
            ui.hyperlink("https://newsapi.org");
        });
    }

    pub fn load_news(&mut self) {
        self.articles.clear();
        let api_key = self.config.api_key.to_string();
        let (mut tx, rx) = std::sync::mpsc::channel();
        let (app_tx, app_rx) = std::sync::mpsc::sync_channel(1);

        self.app_tx = Some(app_tx);

        self.news_rx = Some(rx);

        std::thread::spawn(move || {
            if !api_key.is_empty() {
                fetch_news(&api_key, &mut tx);
            } else {
                loop {
                    match app_rx.recv() {
                        Ok(Msg::ApiKeySet(api_key)) => {
                            fetch_news(&api_key, &mut tx);
                            break;
                        }
                        Err(_) => {}
                    }
                }
            }
        });
    }
}

pub struct NewsCardData {
    pub title: String,
    pub desc: String,
    pub url: String,
}

pub fn fetch_news(api_key: &str, tx: &mut std::sync::mpsc::Sender<NewsCardData>) {
    if let Ok(response) = NewsApi::new(&api_key).country(newsapi::Country::Pl).fetch() {
        let resp_articles = response.articles();
        for a in resp_articles.iter() {
            let news = NewsCardData {
                title: a.title().to_string(),
                desc: a.desc().map(|s| s.to_string()).unwrap_or("...".to_string()),
                url: a.url().to_string(),
            };
            tx.send(news).unwrap_or_else(|e| {
                tracing::error!("Error sending news data: {}", e);
                ()
            });
        }
    }
}

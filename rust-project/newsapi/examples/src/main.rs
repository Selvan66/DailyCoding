mod theme;

use dotenv::dotenv;
use std::error::Error;

use newsapi::{Article, Country, Endpoint, NewsApi};

fn render_articles(articles: &Vec<Article>) {
    let theme = theme::default();
    theme.print_text("# Top headlines\n\n");

    for i in articles {
        theme.print_text(&format!("`{}`", i.title()));
        theme.print_text(&format!("> *{}*", i.url()));
        theme.print_text("---");
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    dotenv();

    let api_key = std::env::var("API_KEY")?;

    let response = NewsApi::new(&api_key)
        .endpoint(Endpoint::TopHeadlines)
        .country(Country::Pl)
        .fetch_async()
        .await?;

    render_articles(&response.articles());

    Ok(())
}

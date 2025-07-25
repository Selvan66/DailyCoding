use std::cell::{RefCell, RefMut};

trait ComponentVec {
    fn as_any(&self) -> &dyn std::any::Any;
    fn as_any_mut(&mut self) -> &mut dyn std::any::Any;
    fn push_none(&mut self);
}

impl<T: 'static> ComponentVec for RefCell<Vec<Option<T>>> {
    fn as_any(&self) -> &dyn std::any::Any {
        self as &dyn std::any::Any
    }

    fn as_any_mut(&mut self) -> &mut dyn std::any::Any {
        self as &mut dyn std::any::Any
    }

    fn push_none(&mut self) {
        self.get_mut().push(None);
    }
}

struct World {
    entities_count: usize,
    component_vecs: Vec<Box<dyn ComponentVec>>,
}

impl World {
    fn new() -> Self {
        Self {
            entities_count: 0,
            component_vecs: Vec::new(),
        }
    }

    fn new_entity(&mut self) -> usize {
        let entity_id = self.entities_count;
        for component_vec in self.component_vecs.iter_mut() {
            component_vec.push_none();
        }

        self.entities_count += 1;
        entity_id
    }

    fn add_component_to_entity<ComponentType: 'static>(
        &mut self,
        entity: usize,
        component: ComponentType,
    ) {
        for component_vec in self.component_vecs.iter_mut() {
            if let Some(component_vec) = component_vec
                .as_any_mut()
                .downcast_mut::<RefCell<Vec<Option<ComponentType>>>>()
            {
                component_vec.get_mut()[entity] = Some(component);
                return;
            }
        }

        let mut new_component_vec: Vec<Option<ComponentType>> =
            Vec::with_capacity(self.entities_count);

        for _ in 0..self.entities_count {
            new_component_vec.push(None);
        }

        new_component_vec[entity] = Some(component);
        self.component_vecs
            .push(Box::new(RefCell::new(new_component_vec)));
    }

    fn borrow_component_vec<ComponentType: 'static>(
        &self,
    ) -> Option<RefMut<Vec<Option<ComponentType>>>> {
        for component_vec in self.component_vecs.iter() {
            if let Some(component_vec) = component_vec
                .as_any()
                .downcast_ref::<RefCell<Vec<Option<ComponentType>>>>()
            {
                return Some(component_vec.borrow_mut());
            }
        }
        None
    }
}

#[derive(Debug)]
struct Health(i32);
struct Name(&'static str);

struct Power(i32);

fn main() {
    let mut world = World::new();

    let entity0 = world.new_entity();
    let entity1 = world.new_entity();
    world.add_component_to_entity(entity0, Health(0));
    world.add_component_to_entity(entity0, Name("Perseus"));
    world.add_component_to_entity(entity1, Health(1));
    world.add_component_to_entity(entity1, Power(100));

    let mut healths = world.borrow_component_vec::<Health>().unwrap();
    let mut names = world.borrow_component_vec::<Name>().unwrap();
    let zip = healths.iter_mut().zip(names.iter_mut());
    let iter = zip.filter_map(|(health, name)| Some((health.as_mut()?, name.as_mut()?)));

    for (health, name) in iter {
        if name.0 == "Perseus" && health.0 <= 0 {
            *health = Health(100);
        }
    }

    let name_iter = names.iter_mut().filter_map(|name| Some(name.as_ref()?));

    for name in name_iter {
        println!("{:?}", name.0);
    }
}

#This function only need to create db or add default data. Use it before another action
def create_documents(cats_collection):

  cats_data = [
      {
          "name": "barsik",
          "age": 3,
          "features": ["ходить в капці", "дає себе гладити", "рудий"]
      },
      {
          "name": "murzik",
          "age": 5,
          "features": ["любить спати на подушці", "чорний"]
      },
      {
          "name": "bobik",
          "age": 2,
          "features": ["постійно голодний", "сірий"]
      },
      {
          "name": "Pusik",
          "age": 4,
          "features": ["лінивий", "любить гуляти", "помаранчевий"]
      },
      {
          "name": "Eindritte",
          "age": 7,
          "features": ["любить командувати","сміливий", "сірий з чорними пʼятнами"]
      }
  ]

  cats_collection.insert_many(cats_data)
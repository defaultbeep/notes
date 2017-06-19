var cats = [
  {
    name: 'Tiggs',
    age: 14
  },
  {
    name: 'Thomas',
    age: 7
  },
  {
    name: 'Socks',
    age: 5
  }
]

/* Map  - transform an array */

let ages = cats.map(c => c.age)

/* Filter - select elements that return true */

let youngCats = cats.filter(c => c.age < 10)

/* Find - selects first element that where callback returns true */

let cat = cats.find(c => c.name === 'Tiggs')


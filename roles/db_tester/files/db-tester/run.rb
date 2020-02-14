#!/usr/bin/env ruby

require "sequel"

DB = Sequel.postgres(host: 'db1', user: 'test', password: 'test', database: 'test')

# create an items table
DB.create_table?(:items) do
  primary_key :id
  String :name, null: false
  Float :price, null: false
end

# create a dataset from the items table
items = DB[:items]

num_of_rows = ARGV.fetch(0, 100).to_i
rows = num_of_rows.times.map { { name: Array.new(10) { ('a'.ord + rand(26)).chr }.join, price: rand(100) } }

items.multi_insert(rows)

puts "Item count: #{items.count}"
puts "The average price is: #{items.avg(:price)}"

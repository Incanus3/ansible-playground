#!/usr/bin/env ruby

require "sequel"

DB = Sequel.postgres(host: 'db-master', user: 'test', password: 'test', database: 'test')

items = DB[:test]

max = items.max(:number)

puts "max value: #{max}"

all_values = items.select_map(:number)

puts "all values:"
p all_values

missing_values = []

1.upto(max) do |val|
  missing_values << val unless all_values.include?(val)
end

puts "missing values:"
p missing_values

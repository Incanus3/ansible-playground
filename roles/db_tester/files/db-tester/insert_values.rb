#!/usr/bin/env ruby

require "sequel"

DB = Sequel.postgres(host: 'db-master', user: 'test', password: 'test', database: 'test')

DB.drop_table?(:test)

DB.create_table(:test) do
  primary_key :id
  Integer :number, null: false
end

items = DB[:test]

begin
  (0..).each do |i|
    puts "inserting #{i}"
    items.insert(number: i)
  rescue Sequel::DatabaseDisconnectError, Sequel::DatabaseConnectionError => e
    p e
    redo
  rescue Sequel::DatabaseError => e
    p e
    if e.cause.is_a? PG::ReadOnlySqlTransaction
      redo
    else
      raise
    end
  end
rescue Interrupt
end

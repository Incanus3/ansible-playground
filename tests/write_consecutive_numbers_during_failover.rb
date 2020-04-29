require 'awesome_print'
require 'faraday'
require 'faraday_middleware'

base_url = ENV.fetch('BACKEND_URL',  'http://kredit-backend.example.com')
username = ENV.fetch('BACKEND_USER', 'alto')
password = ENV.fetch('BACKEND_PASS', 'alto')
timeout  = ENV.fetch('BACKEND_TIMEOUT', 3)

options = {
  url: base_url,
  headers: { 'Content-Type' => 'application/json',
             'Accept'       => 'application/json' }
}

backend = Faraday.new(options) do |conn|
  conn.request  :json
  conn.response :json, content_type: /\bjson$/
end

token = backend.post('/auth/get_token', username: username, password: password).body['token']

backend.headers = { 'Authorization' => "Token #{token}" }

client_id = backend.get('/kredit/crud/clients').body['results']['clients'].first['id']

begin
  (1..).each do |i|
    response = backend.post('/kredit/crud/transactions',
                            client: client_id, kind: 'KC', amount: 10, description: i,
                            request: { open_timeout: timeout, timeout: timeout })
    ap response.status
    ap response.body
    # sleep 1
    redo unless response.status == 201
  rescue Faraday::TimeoutError => e
    ap e
    redo
  end
rescue Interrupt
  puts "INTERRUPTED"
end

require 'json'
require 'rsemantic'

documents = ["The cat in the hat disabled",
             "A cat is a fine pet ponies.",
             "Do and cats make good pets.",
             "I haven't got a hat."]

i = 0

Dir.glob('../data/court-opinions/*.json') do |data_file|
    file = File.read(data_file)
    data_hash = JSON.parse(file)
    relevant_text = data_hash['plain_text'].gsub('\n', '')
    documents[i] = relevant_text
    i = i + 1
end

puts "Done with Parsing!"


#Log to stdout how the matrix gets built and transformed
search = RSemantic::Search.new(documents, :verbose => false)

#Find documents that are related to documents[0] with a ranking for how related they are.
#puts search.related(0)
puts search.related(0).first(100)

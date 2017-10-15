require 'json'
require 'rsemantic'

documents = ["The cat in the hat disabled",
             "A cat is a fine pet ponies.",
             "Do and cats make good pets.",
             "I haven't got a hat."]

i = 0
key_words = ["market", "manipulation", "stock", "fraud", "invest", "money", "posed", "company"]

Dir.glob('../data/court-opinions/*.json') do |data_file|
    file = File.read(data_file)
    data_hash = JSON.parse(file)
    relevant_text = data_hash['plain_text'].gsub('\n', '')

    array = relevant_text.split do |word|
        key_words.each do |key|
            if word.include? key then
                word = ""
            end
        end
    end

    pruned_text = array.join(" ")

    documents[i] = pruned_text
    i = i + 1

    if i > 1000 then
        break
    end

end

puts "Done with Parsing!"


#Log to stdout how the matrix gets built and transformed
search = RSemantic::Search.new(documents, :verbose => true)

#Find documents that are related to documents[0] with a ranking for how related they are.
#puts search.related(0)
puts search.related(0).first(100)

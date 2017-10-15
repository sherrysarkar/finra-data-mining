require 'json'
require 'rsemantic'

documents = ["The cat in the hat disabled",
             "A cat is a fine pet ponies.",
             "Do and cats make good pets.",
             "I haven't got a hat."]

document_file_paths = []

i = 0
#key_words = ["market", "manipulation", "stock", "fraud", "invest", "company"]
key_words = ["drug", "cocaine", "meth", "Rico", "ring", "cartel", "crack", "Mexican", "traffic"]

Dir.glob('../data/court-opinions/*.json') do |data_file|
    document_file_paths[i] = data_file

    file = File.read(data_file)
    data_hash = JSON.parse(file)
    relevant_text = data_hash['plain_text'].gsub('\n', '') # change to lower case

    array = relevant_text.split
    frequency = Hash.new 0

    array.each do |word|
        key_words.each do |key|
            if word.include? key then
                frequency[key] = frequency[key] + 1
            end
        end
    end

    if frequency.any? then
        pruned_text = ""

        frequency.keys.each do |key|
            frequency[key].times do
                pruned_text.concat(" #{key}")
            end
        end

        documents[i] = pruned_text
        i = i + 1
    end

    if i > 1000 then
        break
    end

end

puts "Done with Parsing!"

#Log to stdout how the matrix gets built and transformed
search = RSemantic::Search.new(documents, :verbose => false)

#Find documents that are related to documents[0] with a ranking for how related they are.
#puts search.related(0)
related_to_zero = search.related(0)

puts "File 0 = #{document_file_paths[0]}"

x = 0
related_to_zero.each do |entry|
    if entry > 0.8
        puts "File : #{document_file_paths[x]}           Correlation : #{entry}"
    end
    x = x + 1
end

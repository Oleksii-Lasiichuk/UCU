let = ["a", "v", "m", "m"]
word = "avm"
word = [i for i in word]

for char in word:
    if char in let:
        let.remove(char)
        print(let)

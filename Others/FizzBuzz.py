def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output+= "Fizz"
            if i % 5 == 0:
                output+= "Buzz"
            if not output:
                output= str(i)
            res.append(output)
        return res

def HashedfizzBuzz(self, n: int) -> List[str]:
        dictionary = { 3: "Fizz",
                       5: "Buzz" }
        res = []
        for i in range(1, n+1):
            output = ""
            for key, value in dictionary.items():
                if i % key == 0:
                    output += value
            if not output:
                output = str(i)
            res.append(output)
                
        return res
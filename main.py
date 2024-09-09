from pymium import Space, PyWindow, Element, Types
space = Space("Calculator")

elementout = Element(Types.h1, innerHTML="Output: 0")
space.append(elementout)

def e(addad):
    print(2)
    addad = addad.innerHTML
    print(addad)
    output = elementout.innerHTML[8:]

    if addad == "+":
        if output[-1] == "+" or output =="0":
            return
    if addad == "=":
        elementout.innerHTML = "Output: "+ str(eval(output))
        window.set_html(space)  
        return
    if addad == "<":
        if len(output)>0:
            elementout.innerHTML = "Output: "+ output[:-1]
            window.set_html(space)  
            return
        
    if output == "0": output=""
    sumoutput = output + str(addad)
    elementout.innerHTML = "Output: "+ sumoutput
    window.set_html(space)  

for i in [1,2,3,4,5,6,7,8,9,0,"+","-","/","*","=","<"]:
    element = Element(Types.button,innerHTML=str(i),id=str(i), onclick=e)
    space.append(element)

window = PyWindow(space)
window.run()
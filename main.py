from pymium import Space, PyWindow, Element, Types
space = Space("Calculator")

elementout = Element(Types.h1, innerHTML="Output: 0")
space.append(elementout)

def e(addad):
    
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




element = Element(Types.button, innerHTML="1", id="1", onclick=lambda: e(1))
space.append(element)
element = Element(Types.button, innerHTML="2", id="2", onclick=lambda: e(2))
space.append(element)
element = Element(Types.button, innerHTML="3", id="3", onclick=lambda: e(3))
space.append(element)
element = Element(Types.button, innerHTML="4", id="4", onclick=lambda: e(4))
space.append(element)
element = Element(Types.button, innerHTML="5", id="5", onclick=lambda: e(5))
space.append(element)
element = Element(Types.button, innerHTML="6", id="6", onclick=lambda: e(6))
space.append(element)
element = Element(Types.button, innerHTML="7", id="7", onclick=lambda: e(7))
space.append(element)
element = Element(Types.button, innerHTML="8", id="8", onclick=lambda: e(8))
space.append(element)
element = Element(Types.button, innerHTML="9", id="9", onclick=lambda: e(9))
space.append(element)
element = Element(Types.button, innerHTML="0", id="0", onclick=lambda: e(0))
space.append(element)
element = Element(Types.button, innerHTML="+", id="+", onclick=lambda: e("+"))
space.append(element)
element = Element(Types.button, innerHTML="-", id="-", onclick=lambda: e("-"))
space.append(element)
element = Element(Types.button, innerHTML="*", id="*", onclick=lambda: e("*"))
space.append(element)
element = Element(Types.button, innerHTML="/", id="/", onclick=lambda: e("/"))
space.append(element)
element = Element(Types.button, innerHTML="<", id="<", onclick=lambda: e("<"))
space.append(element)
element = Element(Types.button, innerHTML="=", id="=", onclick=lambda: e("="))
space.append(element)


window = PyWindow(space)
window.run()
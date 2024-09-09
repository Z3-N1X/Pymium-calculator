from pymium import Space, PyWindow, Element, Types
space = Space("Calculator")

elementout = Element(Types.h1, innerHTML="Output: 0")
space.append(elementout)

def e(addad):
    
    output = elementout.innerHTML[8:]
    if output == "0": output=""
    sumoutput = output + str(addad)
    elementout.innerHTML = "Output: "+ sumoutput
    window.set_html(space)  



x = lambda i: e(i)
element = Element(Types.button, innerHTML="1", id="1", onclick=lambda: x(1))
space.append(element)
element = Element(Types.button, innerHTML="2", id="2", onclick=lambda: x(2))
space.append(element)
element = Element(Types.button, innerHTML="3", id="3", onclick=lambda: x(3))
space.append(element)
element = Element(Types.button, innerHTML="4", id="4", onclick=lambda: x(4))
space.append(element)
element = Element(Types.button, innerHTML="5", id="5", onclick=lambda: x(5))
space.append(element)
element = Element(Types.button, innerHTML="6", id="6", onclick=lambda: x(6))
space.append(element)
element = Element(Types.button, innerHTML="7", id="7", onclick=lambda: x(7))
space.append(element)
element = Element(Types.button, innerHTML="8", id="8", onclick=lambda: x(8))
space.append(element)
element = Element(Types.button, innerHTML="9", id="9", onclick=lambda: x(9))
space.append(element)
element = Element(Types.button, innerHTML="0", id="0", onclick=lambda: x(0))
space.append(element)



window = PyWindow(space)
window.run()
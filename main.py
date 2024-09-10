from pymium import Space, PyWindow, Element, Types, Style

space = Space("Calculator")
output_style = Style(border="solid", border_color="black", border_radius="10px")

elementout = Element(Types.div, className="output", innerHTML="0")
space.append(elementout)

css = """button {
  background-image: linear-gradient(to bottom, #333, #555);
  border: 2px solid #666;
  border-radius: 10px;
  color: #fff;
  cursor: pointer;
  transition: border-color 0.3s ease-in-out;
  margin:3px;
}

button:hover {
  border-color: rgb(255, 0, 0); /* red */
  animation: border-animation 1s infinite;
}

@keyframes border-animation {
  0% {
    border-color: rgb(255, 0, 0); /* red */
  }
  50% {
    border-color: rgb(0, 255, 0); /* green */
  }
  100% {
    border-color: rgb(0, 0, 255); /* blue */
  }
}
.output {
  background-color: #333;
  border-radius: 10px;
  padding: 20px;
  font-family: 'Monaco', monospace;
  font-size: 14px;
  line-height: 1.5;
  color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  overflow: auto;
}

.output::before {
  content: "Output: ";
  font-weight: bold;
  color: #66d9ef;
}"""
space.add_custom_css(css)
button_style = Style(width="40px",height="40px")

def e(addad):
    addad = addad.innerHTML
    output = elementout.innerHTML

    if addad == "+":
        if output[-1] == "+" or output =="0":
            return
    if addad == "=":
        elementout.innerHTML = str(eval(output))
        window.set_html(space)  
        return
    if addad == "<":
        if len(output)>0:
            elementout.innerHTML = output[:-1]
            window.set_html(space)  
            return
        
    if output == "0": output=""
    sumoutput = output + str(addad)
    elementout.innerHTML = sumoutput
    window.set_html(space)  

main_wrapper = Element(Types.div, id="main-wrapper",style = Style(display="flex",flex_wrap="wrap", justify_content="center",align_items="center"))
space.append(main_wrapper)

for i in [1,2,3,"+",4,5,6,"-",7,8,9,"*","<",0,"/","="]:
    element = Element(Types.button,innerHTML=str(i),id=str(i), onclick=e,style = button_style)
    main_wrapper.append(element)

window = PyWindow(space,width=220,height=262,always_on_top=True)
window.run()
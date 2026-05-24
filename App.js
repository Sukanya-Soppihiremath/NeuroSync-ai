import "./App.css";

import axios from "axios";

import {useState} from "react";

function App(){

const[prompt,setPrompt]=useState("");

const[messages,setMessages]=useState([]);


const sendMessage=async()=>{

if(!prompt)return;


const userMsg={

role:"user",

text:prompt

};

setMessages(

prev=>[

...prev,

userMsg

]

);


const response=

await axios.post(

"http://127.0.0.1:8000/chat",

{

prompt

}

);


const aiMsg={

role:"ai",

text:

response.data.response

};

setMessages(

prev=>[

...prev,

aiMsg

]

);

setPrompt("");

};


return(

<div className="container">

<div className="sidebar">

<h1>

NeuroSync AI

</h1>

<p>

Multi Agent Assistant

</p>

<ul>

<li>Chat</li>

<li>Agents</li>

<li>Memory</li>

<li>Tasks</li>

<li>Settings</li>

</ul>

</div>


<div className="chat">

<div className="messages">

{

messages.map(

(msg,index)=>(

<div

key={index}

className=

{msg.role}

>

{msg.text}

</div>

)

)

}

</div>


<div className=

"input-area"

>

<input

value={prompt}

onChange={

e=>

setPrompt(

e.target.value

)

}

/>

<button

onClick=

{sendMessage}

>

Send

</button>

</div>

</div>

</div>

)

}

export default App;
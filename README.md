# General-Purpose AI Desktop Client

Lets users extend the functionality of a given local app by allowing them to access the app through the client where the user can express ideas through prompting.

---

## How Does This Work?

### **Prompt Processing**
When the user enters a prompt, the client sends it to the AI model along with relevant context (e.g., current screen, active application, system capabilities, previous actions).

### **Intent & Context Analysis**
The AI interprets the user’s intent and determines which local tools or data sources are needed. This includes identifying operations such as:

- reading calendar events  
- generating files (e.g., Excel spreadsheets)  
- interacting with local applications  
- performing data transformations  

### **Tool Invocation Layer**
The client exposes a controlled set of tool APIs (e.g., calendar access, file creation, filesystem I/O). The AI does not access the OS directly. It generates structured function calls that the client validates and executes.

### **Execution & Feedback Loop**
After the client executes the tool calls, the results (data, file paths, error messages, etc.) are returned to the AI. The model then:

- interprets the results  
- decides the next step  
- continues the workflow until the task is complete  

This creates an iterative loop allowing the AI to plan, act, verify, and refine its output.

### **Output Generation**

Finally, the AI presents the completed task to the user. Output can take many forms, depending on the what the client is used for, output can be seen in the underlying application accessed or simply in the CLI.

---

## Latest Snapshot

Now includes intuitive interaction with the system calendar. You may access your system calendar (on any OS) through the client, effectively extending the capabilities of the standalone calendar.

### **Example Prompts**
- _"Make a timetable in Excel for piano lessons using calendar"_  
- _"I'm feeling stuck today, can you suggest a productive schedule?"_

### **Screenshots**
![screenshot](prompt_example.png)

# PeripheralAgent
Agent that can mimic human computer use by simple keymouse action. For more agent ability, we use LLM such as deepseek to add or modify keymouse action to have a low cost realization without GPU.


1. excel use example:

<div>
	<p align="center">
  <img alt="Animation Demo" src="https://github.com/elenalulu/PeripheralAgent/blob/main/docs/excel.png" width="660" />
  </p>
</div>

<br>
2. ppt use example:
<div>
	<p align="center">
  <img alt="Animation Demo" src="https://github.com/elenalulu/PeripheralAgent/blob/main/docs/ppt.png" width="660" />
  </p>
</div>


## Install
1. download https://github.com/elenalulu/PeripheralAgent
2. conda create -n keymouse python=3.10
3. conda activate keymouse
4. cd PeripheralAgent
5. pip install -r requirements-windows.txt


## How to use
1. record your repetitive action by KeymouseGo.exe
   a. open KeymouseGo.exe in keymousego folder
   b. click the Record button to start recording
   c. perform any actions on the computer, such as clicking the mouse or typing on the keyboard
   d. click the End button to stop recording
   <div>
	<p align="center">
  <img alt="Animation Demo" src="https://github.com/elenalulu/PeripheralAgent/blob/main/docs/use_record.png" width="660" />
  </p>
</div>

2. add more action through asking LLM, there is an api example in action_deepseek.py
   put the action json in ./keymousego/scripts by sequence
    <div>
	<p align="center">
  <img alt="Animation Demo" src="https://github.com/elenalulu/PeripheralAgent/blob/main/docs/use_deepseek.png" width="660" />
  </p>
</div>

3. then run the command in terminal: python peripheral_agent.py
   you can ajust your scripts by hand or by LLM to optimize the effect
4. there is a demo scripts by simply python demo.py without record actions 


## PPT demo
you can record your own action to create and modify a PPT file with this project.
Here is an example to simplify the record process:
1. cd ppt_demo
2. python record_jsons_ppt.py 
3. python agent_ppt_demo.py

if you want to create your own ppt content by deepseek, please modify the record_jsons_ppt.py by filling in the api and free the code available.

<video width="630" height="300" src="https://github.com/user-attachments/assets/e8cd815e-096f-4a2c-980a-ca8d0bdc654b"></video>


## Contact
<div>
  <p align="center">
  <img alt="Animation Demo" src="https://github.com/elenalulu/PeripheralAgent/blob/main/docs/wechat.jpg" width="200" />
  </p>
</div>

## Reference
Thanks for https://github.com/taojy123/KeymouseGo, for any detail about keymousego, please read the project.


## License

The product is licensed under The Apache License 2.0, which allows for free commercial use. Please include the link to PaperChat and the licensing terms in your product description.


## Contribute

The project code is still quite raw. If anyone makes improvements to the code, we welcome contributions back to this project.
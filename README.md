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
2. add more action through asking LLM, there is an api example in action_deepseek.py
   put the action json in ./keymousego/scripts by sequence
3. then run the command in terminal: python peripheral_agent.py
   you can ajust your scripts by hand or by LLM to optimize the effect
4. there is a demo scripts by simply python peripheral_agent.py without record actions 
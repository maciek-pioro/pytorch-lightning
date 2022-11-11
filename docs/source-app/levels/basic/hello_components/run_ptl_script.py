# app.py
# !curl https://bit.ly/demoLightningScriptpy -o pl_boring_script.py
import lightning as L
from lightning.app.components.training import LightningTrainerScript

# run script that trains PyTorch with the Lightning Trainer
model_script = 'pl_boring_script.py'
component = LightningTrainerScript(
   model_script,
   num_nodes=1,
   cloud_compute=L.CloudCompute("gpu")
)
app = L.LightningApp(component)
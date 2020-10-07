import json
import os

# Config data defines and functions

STORAGE = 'local'  # local, drive, or gcs

CFG_FILE = 'mynewsfeed.cfg'
CFG_INIT = {
  'sites' : ['theguardian.com'], 
  'topics': ['tech'], 
  'seen'  : {},
}
cfg_data = CFG_INIT

if STORAGE == 'drive':
  DRIVE_ROOT = '/content/gdrive'
  cfg_file = DRIVE_ROOT + '/My Drive/' + CFG_FILE
  drive.mount(DRIVE_ROOT)
elif STORAGE == 'gcs':
  cfg_file = 'gs://mynewsfeed/' + CFG_FILE
elif STORAGE == 'local':
  cfg_file = CFG_FILE

# Save the sites and topics...
def save_cfg(file=cfg_file, data=None):
  if not data:
    data = cfg_data
  with open(file, 'w') as f:
    f.write(json.dumps(data))

# Load the sites and topics...
def load_cfg(file=cfg_file):
  if not os.path.exists(file):
    save_cfg(file)
  with open(file, 'r') as f:
    return json.loads(f.read())

def reset_cfg():
  cfg_data = CFG_INIT
  save_cfg()


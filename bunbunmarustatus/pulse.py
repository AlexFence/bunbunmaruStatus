import pulsectl
from .module import Module

class PulseAudio(Module):
    def __init__(self):
        super().__init__()
        self.pulse = pulsectl.Pulse()

    def get_block(self):
        sink = self.pulse.sink_list()[0]
        volume = sink.volume.value_flat * 100
        if sink.mute == 0:
            text = str(volume).split(".")[0] + "%"
        else: 
            text = "muted"

        return {"full_text": text}

    @staticmethod
    def get_name():
        return "pulse"

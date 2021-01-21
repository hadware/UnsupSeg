from dataloader import WavPhnDataset
from pathlib import Path

dataset_path = Path("/scratch1/data/derived_data/HD_PARK_HOSPITAL/other/timit_sampa_5s")

for split in ("train", "val", "test"):
    split_path = dataset_path / Path(split)
    
    dataset = WavPhnDataset(str(split_path))
    for i, (audio, times, phonemes, wav_path) in enumerate(dataset):
        if phonemes:
            print(f"{split} : {i} OK")
        else:
            print(f"Empty phonemes for {wav_path}")

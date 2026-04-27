# Signature Forgery Detection using Siamese Neural Networks

## Overview  
This project implements an offline signature verification system using a Siamese Convolutional Neural Network (CNN). The model compares two signature images and determines whether they belong to the same person (genuine) or if one is forged.  

The system automates signature verification without manual feature extraction, making it efficient and scalable.

---

## Features  
- Siamese Neural Network architecture  
- Image preprocessing (grayscale, resizing, normalization)  
- Similarity-based comparison  
- Desktop-based application  
- Fast and lightweight inference  

---

## Tech Stack  
- Python  
- TensorFlow / Keras  
- NumPy  
- OpenCV  
- Pillow  

---

## Project Structure  

Signature_Forgery_Checker/
│
├── app/
│   ├── main.py
│   ├── predict_siamese.py
│   ├── flask_app.py        
│
├── templates/
│   └── index.html
│
├── assets/
│   └── screenshots/
│       ├── app.png
│       ├── genuine.png
│       ├── forged.png
│
├── sample_inputs/
│   ├── test.png
│   ├── test1.png
│   ├── test2.png
│
├── requirements.txt
├── README.md
├── .gitignore
├── run_app.command

---

## How It Works  

1. Two signature images are given as input  
2. Both images pass through identical CNN branches  
3. The network extracts feature embeddings  
4. A similarity score is computed  
5. Based on a threshold, the output is classified as:  
   - Genuine  
   - Forged  

---

## How to Run  

1. Install dependencies  
pip3 install -r requirements.txt  

2. Run the application  
python3 app/ui.py  

---

## Results  

- The model can differentiate between genuine and forged signatures  
- Performance depends on dataset quality and training balance  
- Threshold tuning improves accuracy  

---

## Future Improvements  

- Use a larger dataset  
- Improve robustness to variations  
- Add real-time signature capture  
- Deploy as mobile or web app  

---

## Author  

Samhit Reddy  
Manipal Institute of Technology  

---

## Notes  

- Model file is not included due to size  
- Can be shared separately if needed

## Demo

- Application Interface

<img width="765" height="392" alt="App UI" src="https://github.com/user-attachments/assets/c25a6760-23eb-4630-a7b1-e95b8e44fb2e" />


- Genuine Detection

<img width="757" height="618" alt="Genuine" src="https://github.com/user-attachments/assets/56014bbf-5637-43c8-9624-57d6812c5bb2" />


- Forged Detection

<img width="740" height="622" alt="Forged" src="https://github.com/user-attachments/assets/5b1f1e85-e4fa-4033-946d-ba4af51a5390" />



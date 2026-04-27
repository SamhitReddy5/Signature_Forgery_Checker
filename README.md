# Signature Forgery Detection using Siamese Neural Networks

## Overview  
This project implements an offline signature verification system using a Siamese Convolutional Neural Network (CNN). The system compares two signature images and predicts whether they belong to the same person (genuine) or if one is forged.  

The approach uses deep learning to automatically learn features from signatures, avoiding manual feature engineering.

---

## Features  
- Siamese Neural Network architecture  
- Image preprocessing (grayscale, resizing, normalization)  
- Similarity-based comparison  
- Desktop-compatible execution  
- Fast inference  

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

1. Two signature images are provided as input  
2. Both images pass through identical CNN branches  
3. Feature embeddings are extracted  
4. A similarity score is computed  
5. Based on a threshold, the system classifies the result as genuine or forged  

---

## How to Run  

Install dependencies:  
pip3 install -r requirements.txt  

Run the application:  
python3 app/main.py  

---

## Results  

- The model can distinguish between genuine and forged signatures  
- Performance depends on dataset quality and training balance  
- Threshold tuning improves prediction reliability  

---

## Future Improvements  

- Train on a larger dataset  
- Improve robustness to variations in writing style  
- Add real-time signature capture  
- Deploy as a standalone desktop application  

---

## Author  

Samhit Reddy  
Manipal Institute of Technology  

---

## Notes  

- Large model files are not included in this repository  
- The trained model can be shared via external storage if required

## Demo

- Application Interface

<img width="765" height="392" alt="App UI" src="https://github.com/user-attachments/assets/c25a6760-23eb-4630-a7b1-e95b8e44fb2e" />


- Genuine Detection

<img width="757" height="618" alt="Genuine" src="https://github.com/user-attachments/assets/56014bbf-5637-43c8-9624-57d6812c5bb2" />


- Forged Detection

<img width="740" height="622" alt="Forged" src="https://github.com/user-attachments/assets/5b1f1e85-e4fa-4033-946d-ba4af51a5390" />



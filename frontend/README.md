# AI Transcriber Frontend

## 📌 Overview
AI Transcriber Frontend एक आधुनिक और रिस्पॉन्सिव वेब एप्लिकेशन है, जिसे **React.js** का उपयोग करके विकसित किया गया है। यह ऑडियो फ़ाइलों को टेक्स्ट में बदलने के लिए AI-आधारित बैकएंड के साथ इंटीग्रेट किया गया है।

## 🎯 Features
- **यूजर-फ्रेंडली इंटरफेस** - सिंपल और क्लीन UI डिज़ाइन
- **रिस्पॉन्सिव डिज़ाइन** - मोबाइल और डेस्कटॉप दोनों पर शानदार अनुभव
- **रीयल-टाइम ट्रांसक्रिप्शन** - ऑडियो फाइल को तुरंत टेक्स्ट में बदलें
- **मल्टी-लैंग्वेज सपोर्ट** - हिंदी, अंग्रेज़ी और अन्य भाषाओं में ट्रांसक्रिप्शन सपोर्ट
- **फास्ट प्रोसेसिंग** - न्यूनतम लेटेंसी के साथ तेज़ परफॉर्मेंस

## 📂 Project Structure
```
AI-Transcriber/
│
├── frontend/                     # React Frontend Code
│   ├── node_modules/             # Node.js Modules
│   ├── public/                   # Static Files (HTML, CSS, JS)
│   ├── src/                      # React Source Code
│   ├── package.json              
│   ├── package-lock.json         
│   └── README.md                 
│
├── backend/                      # Flask Backend Code
│   ├── uploads/                  # Folder to store uploaded audio files
│   ├── routes/                   # API Routes
│   │   ├── transcribe.py         # Speech-to-Text API
│   │   ├── tts.py                # Text-to-Speech API
│   ├── static/                   # Static Files (if needed)
│   ├── templates/                # HTML Templates (if using Jinja)
│   ├── venv/                     # Python Virtual Environment
│   ├── app.py                    # Main Flask App
│   ├── requirements.txt          # Python Dependencies
│   └── README.md                 
│
├── test_data/                     # Sample Data for Testing
│   ├── fixed_audio.wav           
│   ├── generated_audio.mp3       
│   ├── generated_audio.wav       
│   ├── uploaded_audio.wav        
│   └── output.mp3                
│
├── .gitignore                     
└── README.md                      

```

## 🚀 Installation & Setup
1. **Prerequisites**: सुनिश्चित करें कि आपके सिस्टम में **Node.js** और **npm** इंस्टॉल है।
2. **डिपेंडेंसी इंस्टॉल करें**:
   ```sh
   cd frontend
   npm install
   ```
3. **React ऐप स्टार्ट करें**:
   ```sh
   npm start
   ```
4. **अब ऐप लोकलहोस्ट पर एक्सेस करें**: `http://localhost:3000`

## 🔗 API Integration
यह फ्रंटएंड बैकएंड के साथ कनेक्ट होकर `/transcribe` API को कॉल करता है।

## 🤖 Technologies Used
- **React.js** - UI निर्माण के लिए
- **Fetch API** - बैकएंड से डेटा लेने के लिए
- **Bootstrap / CSS** - स्टाइलिंग के लिए

## 👨‍💻 Contributors
- **Naresh Kumar** *(Lead Developer)*
- और अन्य योगदानकर्ताओं के लिए [CONTRIBUTORS.md](./CONTRIBUTORS.md) देखें।

## 📜 License
यह प्रोजेक्ट **MIT License** के तहत आता है।

---
✅ **AI-आधारित ट्रांसक्रिप्शन को और भी बेहतर बनाएं! 🚀**


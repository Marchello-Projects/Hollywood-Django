// Experts
const phoneElements = {
    imgPhone: document.querySelector("#imgPhone"),
    phoneText1: document.querySelector("#phoneText1"),
    phoneText2: document.querySelector("#phoneText2")
}

import phone1 from './img/experts/phone1.png'
import phone2 from './img/experts/phone2.png'
import phone3 from './img/experts/phone3.png'
import phone4 from './img/experts/phone4.png'
import phone5 from './img/experts/phone5.png'
import phone6 from './img/experts/phone6.png'
import phone7 from './img/experts/phone7.png'
import phone8 from './img/experts/phone8.png'

const arrayImgsPhoneExperts = [
    phone1,
    phone2,
    phone3,
    phone4,
    phone5,
    phone6,
    phone7,
    phone8,
]

const arrayTitleTextPhoneExperts = [
    "Твердохліб Андрій Валерійович",
    "Киселиця Владислав Юрійович",
    "Звягіна Майя Юріївна",
    "Бесчастний Олександр Олександрович",
    "Пашков Валентин Валерійович",
    "Коваль Тетяна Валеріївна",
    "Попеско Анастасія Ігорівна",
    "Олексюк Аліна"
]

const arrayInfoTextPhoneExperts = [
    "Власник клінік, Терапевтичний прийом,Хірургічний прийом,Ортопедичний прийом.",
    "Терапевтичний прийом, Хірургічний прийом, Ортопедичний прийом",
    "Професійний догляд та профілактика.",
    "Терапевтичний прийом, Хірургічний прийом, Ортопедичний прийом",
    "Ортодонтичний прийом",
    "Асистент стоматолога",
    "Терапевтичний прийом, Дитячий прийом, Професійний догляд та профілактика",
    "Адміністратор"
]

let indexImgPhone = 0
let indexTitleTextPhone = 0
let indexInfoTextPhone = 0

setInterval(() => {
    phoneElements.imgPhone.classList.add('hidden')
    phoneElements.phoneText1.classList.add('hidden')
    phoneElements.phoneText2.classList.add('hidden')

    setTimeout(() => {
        if (indexImgPhone != arrayImgsPhoneExperts.length - 1 &&
            indexTitleTextPhone != arrayTitleTextPhoneExperts.length - 1 &&
            indexInfoTextPhone != arrayInfoTextPhoneExperts.length - 1) {
            indexImgPhone += 1
            indexTitleTextPhone += 1
            indexInfoTextPhone += 1
        } else {
            indexImgPhone = 0
            indexTitleTextPhone = 0
            indexInfoTextPhone = 0
        }

        phoneElements.imgPhone.src = arrayImgsPhoneExperts[indexImgPhone];
        phoneElements.phoneText1.textContent = `${arrayTitleTextPhoneExperts[indexTitleTextPhone]}`
        phoneElements.phoneText2.textContent = `${arrayInfoTextPhoneExperts[indexInfoTextPhone]}`

        phoneElements.imgPhone.classList.remove('hidden')
        phoneElements.phoneText1.classList.remove('hidden')
        phoneElements.phoneText2.classList.remove('hidden')
    }, 1000)
}, 3000)

// Slider
const phoneImg = document.querySelector("#phoneImg")
import img1 from './img/works/1.png';
import img2 from './img/works/2.png';
import img3 from './img/works/3.png';

const arrayImgsPhone = [
    img1,
    img2,
    img3,
];

let indexImgPhoneWorks = 0

setInterval(() => {
    phoneImg.classList.add('hidden')

    setTimeout(() => {
        if (indexImgPhoneWorks != arrayImgsPhone.length - 1) {
            indexImgPhoneWorks += 1
        } else {
            indexImgPhoneWorks = 0
        }

        phoneImg.src = arrayImgsPhone[indexImgPhoneWorks];

        phoneImg.classList.remove('hidden')
    }, 1000)
}, 3000)

// Services
let slideIndex = 1;
    
const showSlides = () => {
    const slides = document.getElementsByClassName("phoneMain_block4_bl_forslider3_block")

    Array.from(slides).forEach(slide => {
        slide.classList.add("hidden")
        slide.style.display = "none"
    })

    slideIndex++
    if (slideIndex > slides.length) {
        slideIndex = 1
    }

    const currentSlide = slides[slideIndex - 1]
    currentSlide.style.display = "block"
    setTimeout(() => {
        currentSlide.classList.remove("hidden")
    }, 50)

    setTimeout(showSlides, 3000)
}

showSlides()
// Experts
const tabletElements = {
    tabletImgExpert: document.querySelector("#tabletImgExpert"),
    tabletTitleTextExpert: document.querySelector("#tabletTitleTextExpert"),
    tabletInfoTextExpert: document.querySelector("#tabletInfoTextExpert"),
}

import tablet1 from '/static/img/experts/tablet1.png';
import tablet2 from '/static/img/experts/tablet2.png';
import tablet3 from '/static/img/experts/tablet3.png';
import tablet4 from '/static/img/experts/tablet4.png';
import tablet5 from '/static/img/experts/tablet5.png';
import tablet6 from '/static/img/experts/tablet6.png';
import tablet7 from '/static/img/experts/tablet7.png';
import tablet8 from '/static/img/experts/tablet8.png';

const arrayImgsTabletExperts = [
    tablet1,
    tablet2,
    tablet3,
    tablet4,
    tablet5,
    tablet6,
    tablet7,
    tablet8,
];

const arrayTitleTextTabletExperts = [
    "Твердохліб Андрій Валерійович",
    "Киселиця Владислав Юрійович",
    "Звягіна Майя Юріївна",
    "Бесчастний Олександр Олександрович",
    "Попеско Анастасія Ігорівна",
    "Пашков Валентин Валерійович",
    "Коваль Тетяна Валеріївна",
    "Олексюк Аліна"
]

const arrayInfoTextTabletExperts = [
    "Власник клінік, Терапевтичний прийом,Хірургічний прийом,Ортопедичний прийом.",
    "Терапевтичний прийом, Хірургічний прийом, Ортопедичний прийом",
    "Професійний догляд та профілактика.",
    "Терапевтичний прийом, Хірургічний прийом, Ортопедичний прийом",
    "Терапевтичний прийом, Дитячий прийом, Професійний догляд та профілактика",
    "Ортодонтичний прийом",
    "Асистент стоматолога",
    "Адміністратор"
]

let indexImgTablet = 0
let indexTitleTextTablet = 0
let indexInfoTextTablet = 0

setInterval(() => {
    tabletElements.tabletImgExpert.classList.add('hidden')
    tabletElements.tabletTitleTextExpert.classList.add('hidden')
    tabletElements.tabletInfoTextExpert.classList.add('hidden')

    setTimeout(() => {
        if (indexImgTablet != arrayImgsTabletExperts.length - 1 &&
            indexTitleTextTablet != arrayTitleTextTabletExperts.length - 1 &&
            indexInfoTextTablet != arrayInfoTextTabletExperts.length - 1) {
            indexImgTablet += 1
            indexTitleTextTablet += 1
            indexInfoTextTablet += 1
        } else {
            indexImgTablet = 0
            indexTitleTextTablet = 0
            indexInfoTextTablet = 0
        }

        tabletElements.tabletImgExpert.src = arrayImgsTabletExperts[indexImgTablet];
        tabletElements.tabletTitleTextExpert.textContent = `${arrayTitleTextTabletExperts[indexTitleTextTablet]}`
        tabletElements.tabletInfoTextExpert.textContent = `${arrayInfoTextTabletExperts[indexInfoTextTablet]}`

        tabletElements.tabletImgExpert.classList.remove('hidden')
        tabletElements.tabletTitleTextExpert.classList.remove('hidden')
        tabletElements.tabletInfoTextExpert.classList.remove('hidden')
    }, 1000)
}, 3000)


// Slider
const tabletImg = document.querySelector("#tabletImg")

import img1 from './img/worksTablet/1.png';
import img2 from './img/worksTablet/2.png';
import img3 from './img/worksTablet/3.png';

const arrayImgsTablet = [
    img1,
    img2,
    img3,
];

let indexImgTabletWorks = 0

setInterval(() => {
    tabletImg.classList.add('hidden')

    setTimeout(() => {
        if (indexImgTabletWorks != arrayImgsTablet.length - 1) {
            indexImgTabletWorks += 1
        } else {
            indexImgTabletWorks = 0
        }

        tabletImg.src = arrayImgsTablet[indexImgTabletWorks];

        tabletImg.classList.remove('hidden')
    }, 1000)
}, 3000)
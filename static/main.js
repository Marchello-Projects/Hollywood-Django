// Slider
const htmlSliderElements = {
    btnReturn: document.querySelector("#btnReturn"),
    btnNext: document.querySelector("#btnNext"),
    img: document.querySelector("#img")
}
const arrayImgs = [
    '1.png',
    '2.png',
    '3.png',
]
let indexImg = 0
htmlSliderElements.btnReturn.addEventListener("click", () => {
    htmlSliderElements.img.classList.add('hidden')
    setTimeout(() => {
        if (indexImg != 0) {
            indexImg -= 1
        } else {
            indexImg = arrayImgs.length - 1
        }
        htmlSliderElements.img.src = `/static/img/works/${arrayImgs[indexImg]}`
        htmlSliderElements.img.classList.remove('hidden')
    }, 500)
})
htmlSliderElements.btnNext.addEventListener("click", () => {
    htmlSliderElements.img.classList.add('hidden')
    setTimeout(() => {
        if (indexImg != arrayImgs.length - 1) {
            indexImg += 1
        } else {
            indexImg = 0
        }
        htmlSliderElements.img.src = `/static/img/works/${arrayImgs[indexImg]}`
        htmlSliderElements.img.classList.remove('hidden')
    }, 500)
})
// Experts
const htmlExpertsElements = {
    imgExpert1: document.querySelector("#imgExpert1"),
    titleTextExpert1: document.querySelector("#titleTextExpert1"),
    infoTextExpert1: document.querySelector("#infoTextExpert1"),
    imgExpert2: document.querySelector("#imgExpert2"),
    titleTextExpert2: document.querySelector("#titleTextExpert2"),
    infoTextExpert2: document.querySelector("#infoTextExpert2"),
}
const arrayImgsTabletExperts1 = [
    '1.png',
    '3.png',
    '5.png',
    '7.png',
]
const arrayImgsTabletExperts2 = [
    '2.png',
    '4.png',
    '6.png',
    '8.png',
]
let imgIndexBlock1 = 0
let imgIndexBlock2 = 0
const arrayTitleTextExperts1 = [
    "Твердохліб Андрій Валерійович",
    "Звягіна Майя Юріївна",
    "Бесчастний Олександр Олександрович",
    "Олексюк Аліна"
]
const arrayTitleTextExperts2 = [
    "Киселиця Владислав Юрійович",
    "Коваль Тетяна Валеріївна",
    "Попеско Анастасія Ігорівна",
    "Пашков Валентин Валерійович"
]
let textTitleIndex1 = 0
let textTitleIndex2 = 0
const arrayInfoTextExperts1 = [
    "Власник клінік, Терапевтичний прийом,Хірургічний прийом,Ортопедичний прийом.",
    "Професійний догляд та профілактика.",
    "Терапевтичний прийом, Хірургічний прийом, Ортопедичний прийом",
    "Адміністратор"
]
const arrayInfoTextExperts2 = [
    "Терапевтичний прийом, Хірургічний прийом, Ортопедичний прийом",
    "Асистент стоматолога",
    "Терапевтичний прийом, Дитячий прийом, Професійний догляд та профілактика",
    "Ортодонтичний прийом"
]
let textInfoIndex1 = 0
let textInfoIndex2 = 0
setInterval(() => {
    htmlExpertsElements.imgExpert1.classList.add('hidden')
    htmlExpertsElements.imgExpert2.classList.add('hidden')
    htmlExpertsElements.titleTextExpert1.classList.add('hidden')
    htmlExpertsElements.titleTextExpert2.classList.add('hidden')
    htmlExpertsElements.infoTextExpert1.classList.add('hidden')
    htmlExpertsElements.infoTextExpert2.classList.add('hidden')
    setTimeout(() => {
        if (
            imgIndexBlock1 != arrayImgsTabletExperts1.length - 1 &&
            imgIndexBlock2 != arrayImgsTabletExperts2.length - 1 &&
            textTitleIndex1 != arrayTitleTextExperts1.length - 1 &&
            textTitleIndex2 != arrayTitleTextExperts2.length - 1 &&
            textInfoIndex1 != arrayInfoTextExperts1.length - 1 &&
            textInfoIndex2 != arrayInfoTextExperts2.length - 1
        ) {
            imgIndexBlock1 += 1
            imgIndexBlock2 += 1
            textTitleIndex1 += 1
            textTitleIndex2 += 1
            textInfoIndex1 += 1
            textInfoIndex2 += 1
        } else {
            imgIndexBlock1 = 0
            imgIndexBlock2 = 0
            textTitleIndex1 = 0
            textTitleIndex2 = 0
            textInfoIndex1 = 0
            textInfoIndex2 = 0
        }
        htmlExpertsElements.imgExpert1.src = `/static/img/experts/${arrayImgsTabletExperts1[imgIndexBlock1]}`
        htmlExpertsElements.imgExpert2.src = `/static/img/experts/${arrayImgsTabletExperts2[imgIndexBlock2]}`
        htmlExpertsElements.titleTextExpert1.textContent = `${arrayTitleTextExperts1[textTitleIndex1]}`
        htmlExpertsElements.titleTextExpert2.textContent = `${arrayTitleTextExperts2[textTitleIndex2]}`
        htmlExpertsElements.infoTextExpert1.textContent = `${arrayInfoTextExperts1[textInfoIndex1]}`
        htmlExpertsElements.infoTextExpert2.textContent = `${arrayInfoTextExperts2[textInfoIndex2]}`
        htmlExpertsElements.imgExpert1.classList.remove('hidden');
        htmlExpertsElements.imgExpert2.classList.remove('hidden');
        htmlExpertsElements.titleTextExpert1.classList.remove('hidden');
        htmlExpertsElements.titleTextExpert2.classList.remove('hidden');
        htmlExpertsElements.infoTextExpert1.classList.remove('hidden');
        htmlExpertsElements.infoTextExpert2.classList.remove('hidden')
    }, 1000)
}, 3000)

// Experts
const phoneElements = {
    imgPhone: document.querySelector("#imgPhone"),
    phoneText1: document.querySelector("#phoneText1"),
    phoneText2: document.querySelector("#phoneText2")
}
const arrayImgsPhoneExperts = [
    'phone1.png',
    'phone2.png',
    'phone3.png',
    'phone4.png',
    'phone5.png',
    'phone6.png',
    'phone7.png',
    'phone8.png',
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
        phoneElements.imgPhone.src = `/static/phone/img/experts/${arrayImgsPhoneExperts[indexImgPhone]}`
        phoneElements.phoneText1.textContent = `${arrayTitleTextPhoneExperts[indexTitleTextPhone]}`
        phoneElements.phoneText2.textContent = `${arrayInfoTextPhoneExperts[indexInfoTextPhone]}`
        phoneElements.imgPhone.classList.remove('hidden')
        phoneElements.phoneText1.classList.remove('hidden')
        phoneElements.phoneText2.classList.remove('hidden')
    }, 1000)
}, 3000)
// Slider
const phoneImg = document.querySelector("#phoneImg")
const arrayImgsPhone = [
    '1.png',
    '2.png',
    '3.png',
]
let indexImgPhoneWorks = 0
setInterval(() => {
    phoneImg.classList.add('hidden')
    setTimeout(() => {
        if (indexImgPhoneWorks != arrayImgsPhone.length - 1) {
            indexImgPhoneWorks += 1
        } else {
            indexImgPhoneWorks = 0
        }
        phoneImg.src = `/static/phone/img/works/${arrayImgsPhone[indexImgPhoneWorks]}`
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

// Experts
const tabletElements = {
    tabletImgExpert: document.querySelector("#tabletImgExpert"),
    tabletTitleTextExpert: document.querySelector("#tabletTitleTextExpert"),
    tabletInfoTextExpert: document.querySelector("#tabletInfoTextExpert"),
}
const arrayImgsTabletExperts = [
    'tablet1.png',
    'tablet2.png',
    'tablet3.png',
    'tablet4.png',
    'tablet5.png',
    'tablet6.png',
    'tablet7.png',
    'tablet8.png',
]
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
        tabletElements.tabletImgExpert.src = `/static/tablet/img/experts/${arrayImgsTabletExperts[indexImgTablet]}`
        tabletElements.tabletTitleTextExpert.textContent = `${arrayTitleTextTabletExperts[indexTitleTextTablet]}`
        tabletElements.tabletInfoTextExpert.textContent = `${arrayInfoTextTabletExperts[indexInfoTextTablet]}`
        tabletElements.tabletImgExpert.classList.remove('hidden')
        tabletElements.tabletTitleTextExpert.classList.remove('hidden')
        tabletElements.tabletInfoTextExpert.classList.remove('hidden')
    }, 1000)
}, 3000)
// Slider
const tabletImg = document.querySelector("#tabletImg")
const arrayImgsTablet = [
    '1.png',
    '2.png',
    '3.png',
]
let indexImgTabletWorks = 0
setInterval(() => {
    tabletImg.classList.add('hidden')
    setTimeout(() => {
        if (indexImgTabletWorks != arrayImgsTablet.length - 1) {
            indexImgTabletWorks += 1
        } else {
            indexImgTabletWorks = 0
        }
        tabletImg.src = `/static/img/works/${arrayImgsTablet[indexImgTabletWorks]}`
        tabletImg.classList.remove('hidden')
    }, 1000)
}, 3000)
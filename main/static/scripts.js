// // scripts.js
// gsap.registerPlugin(ScrollTrigger);

// // Анимация для текста
// gsap.from(".text-content", {
//     scrollTrigger: {
//         trigger: ".sticky-section",
//         start: "top center",
//         end: "bottom center",
//         scrub: true,
//     },
//     x: -100,
//     opacity: 0,
//     duration: 1,
// });

// // Анимация для изображений
// gsap.from(".image-content", {
//     scrollTrigger: {
//         trigger: ".sticky-section",
//         start: "top center",
//         end: "bottom center",
//         scrub: true,
//     },
//     x: 100,
//     opacity: 0,
//     duration: 1,
// });

// // Анимация для заголовка в видео-секции
// gsap.from(".video-overlay h1", {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     delay: 0.5,
// });

// // Анимация для текста в видео-секции
// gsap.from(".video-overlay p", {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     delay: 1,
// });

// gsap.to(".video-bg", {
//     scrollTrigger: {
//         trigger: ".video-section",
//         start: "top top",
//         end: "bottom top",
//         scrub: true,
//     },
//     y: 100, // Параллакс-эффект
// });
// gsap.to(".sticky-section", {
//     scrollTrigger: {
//         trigger: ".sticky-section",
//         start: "top center",
//         end: "bottom center",
//         scrub: true,
//     },
//     backgroundColor: "#0073e6", // Изменение цвета фона
// });
// gsap.from(".sticky-section", {
//     scrollTrigger: {
//         trigger: ".sticky-section",
//         start: "top 80%",
//         end: "bottom 20%",
//         toggleActions: "play none none reverse",
//     },
//     opacity: 0,
//     y: 50,
//     duration: 1,
// });










// // Регистрируем плагин ScrollTrigger
// gsap.registerPlugin(ScrollTrigger);

// // Анимация для текста в видео-секции
// gsap.from(".video-overlay h1", {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     delay: 0.5,
// });

// gsap.from(".video-overlay p", {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     delay: 1,
// });

// gsap.from(".cta-button", {
//     opacity: 0,
//     y: 50,
//     duration: 1.5,
//     delay: 1.5,
// });

// // Анимация для липких секций
// gsap.from(".text-content", {
//     scrollTrigger: {
//         trigger: ".sticky-section",
//         start: "top center",
//         end: "bottom center",
//         scrub: true,
//     },
//     x: -100,
//     opacity: 0,
//     duration: 1,
// });

// gsap.from(".image-content", {
//     scrollTrigger: {
//         trigger: ".sticky-section",
//         start: "top center",
//         end: "bottom center",
//         scrub: true,
//     },
//     x: 100,
//     opacity: 0,
//     duration: 1,
// });

// // Параллакс для видео-фона
// gsap.to(".video-bg", {
//     scrollTrigger: {
//         trigger: ".video-section",
//         start: "top top",
//         end: "bottom top",
//         scrub: true,
//     },
//     y: 100, // Параллакс-эффект
// });

// Регистрируем плагин ScrollTrigger
// Регистрируем плагин ScrollTrigger

gsap.registerPlugin(ScrollTrigger);

// Анимация для текста в видео-секции
gsap.from(".video-overlay h1", {
    opacity: 0,
    y: 50,
    duration: 1.5,
    delay: 0.5,
});

gsap.from(".video-overlay p", {
    opacity: 0,
    y: 50,
    duration: 1.5,
    delay: 1,
});

gsap.from(".cta-button", {
    opacity: 0,
    y: 50,
    duration: 1.5,
    delay: 1.5,
});

// Анимация для каждой секции
gsap.from(".section-1 .text-content", {
    scrollTrigger: {
        trigger: ".section-1",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: -100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-1 .image-content", {
    scrollTrigger: {
        trigger: ".section-1",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: 100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-2 .text-content", {
    scrollTrigger: {
        trigger: ".section-2",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    y: 100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-2 .image-content", {
    scrollTrigger: {
        trigger: ".section-2",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    y: -100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-3 .text-content", {
    scrollTrigger: {
        trigger: ".section-3",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: 100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-3 .image-content", {
    scrollTrigger: {
        trigger: ".section-3",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: -100,
    opacity: 0,
    duration: 1,
});
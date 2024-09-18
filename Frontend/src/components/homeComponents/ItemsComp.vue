<template>
  <section>
    <article>
      <img src="../../assets/images/pieza1.svg" alt="" />
      <RouterLink
        >VER ARTICULOS
        <span
          ><svg
            class="flechita-header-button"
            width="12"
            height="13"
            viewBox="0 0 12 13"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g clip-path="url(#clip0_5744_10485)">
              <path
                d="M6.79688 2.90625L10.1435 6.25292L6.79688 9.59958"
                stroke="#e5e5e5"
                stroke-width="0.991605"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </g>
            <defs>
              <clipPath id="clip0_5744_10485">
                <rect
                  width="11.8993"
                  height="11.8993"
                  fill="white"
                  transform="translate(0.101562 0.300781)"
                />
              </clipPath>
            </defs></svg></span
      ></RouterLink>
    </article>
    <article>
      <img src="../../assets/images/pieza2.svg" alt="" />
      <RouterLink
        >VER MACETAS
        <span
          ><svg
            class="flechita-header-button"
            width="12"
            height="13"
            viewBox="0 0 12 13"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g clip-path="url(#clip0_5744_10485)">
              <path
                d="M6.79688 2.90625L10.1435 6.25292L6.79688 9.59958"
                stroke="#e5e5e5"
                stroke-width="0.991605"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </g>
            <defs>
              <clipPath id="clip0_5744_10485">
                <rect
                  width="11.8993"
                  height="11.8993"
                  fill="white"
                  transform="translate(0.101562 0.300781)"
                />
              </clipPath>
            </defs></svg></span
      ></RouterLink>
    </article>
    <article>
      <img src="../../assets/images/pieza3.svg" alt="" />
      <RouterLink
        >VER PLANTAS
        <span
          ><svg
            class="flechita-header-button"
            width="12"
            height="13"
            viewBox="0 0 12 13"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g clip-path="url(#clip0_5744_10485)">
              <path
                d="M6.79688 2.90625L10.1435 6.25292L6.79688 9.59958"
                stroke="#e5e5e5"
                stroke-width="0.991605"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </g>
            <defs>
              <clipPath id="clip0_5744_10485">
                <rect
                  width="11.8993"
                  height="11.8993"
                  fill="white"
                  transform="translate(0.101562 0.300781)"
                />
              </clipPath>
            </defs></svg></span
      ></RouterLink>
    </article>
    <article>
      <img src="../../assets/images/pieza4.svg" alt="" />
      <RouterLink
        >VER CACTUS
        <span
          ><svg
            class="flechita-header-button"
            width="12"
            height="13"
            viewBox="0 0 12 13"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g clip-path="url(#clip0_5744_10485)">
              <path
                d="M6.79688 2.90625L10.1435 6.25292L6.79688 9.59958"
                stroke="#e5e5e5"
                stroke-width="0.991605"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </g>
            <defs>
              <clipPath id="clip0_5744_10485">
                <rect
                  width="11.8993"
                  height="11.8993"
                  fill="white"
                  transform="translate(0.101562 0.300781)"
                />
              </clipPath>
            </defs></svg></span
      ></RouterLink>
    </article>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
section {
  padding: 150px 5% 100px;
  background-image: url('../../assets/images/background.jpg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 100px;
}
article {
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  padding: 10px 50px 30px;
  height: max-content;
  width: 100%;
  background-color: #14141463;
  transition: 0.2s ease;
}
article:hover {
  background-color: #141414;
  border-color: #32771f;
}
article:hover a {
  color: #32771f;
  stroke: #32771f;
}
svg path{
    transition: .2s ease;
}
article:hover svg {
  transform: translateX(5px);
}
article:hover svg path {
  stroke: #32771f;
}
article img {
  position: relative;
  top: -100px;
  width: 100px;
  margin-bottom: -60px;
}
article a {
  font-size: calc(0.8rem + 0.2vw);
  font-family: 'Rubik';
  color: #e5e5e5;
  text-decoration: none;
  transition: 0.2s ease;
  overflow-x: visible;
}
svg {
  scale: 1.4;
  position: relative;
  top: 2px;
  transition: 0.2s ease;
}
@media (min-width: 500px) {
  section {
    padding-top: 120px;
  }
  article {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 10px 60px 10px;
    width: 450px;
  }
}
@media (min-width: 700px) {
  section {
    justify-content: center;
    padding-top: 120px;
    flex-direction: row;
    flex-wrap: wrap;
  }
  article {
    flex-direction: column;
    padding: 25px 60px 25px;
    width: 250px;
  }
}
@media (min-width: 900px) {
  section {
    gap: 80px;
  }
  article {
    width: 350px;
  }
  article img {
    scale: 1.2;
  }
}
@media (min-width: 1000px) {
  section {
    gap: 80px;
  }
  article {
    width: 400px;
  }
}
@media (min-width: 1200px) {
  section {
    flex-wrap: nowrap;
    justify-content: space-between;
    gap: 40px;
  }
  article {
    width: 300px;
  }
  article img {
    scale: 1;
    width: 100%;
    margin-bottom: -40px;
  }
}
</style>

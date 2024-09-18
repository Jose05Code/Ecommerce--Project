<template>
  <header>
    <div class="header-text-container">
      <div class="header-text">
        <h1>Lorem ipsum dolor sit amet consectetur adipisicing elit.</h1>
      </div>
      <div class="header-button-container">
        <p>
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur natus cum, explicabo vel architecto quis ex labore doloribus!
        </p>
        <RouterLink class="header-button"
          >Ir al Catalogo
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
                  stroke="#141414"
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
              </defs>
            </svg> </span
        ></RouterLink>
      </div>
    </div>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
header {
  margin-top: 60px;
  padding: 10% 0;
  display: flex;
  align-items: center;
  background-image: url('../../assets/images/banner.jpg');
  background-position: bottom;
  background-size: cover;
  background-repeat: no-repeat;
  height: 800px;
  width: 100%;
}
.header-text-container{
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(228, 226, 226, 0.486);
  padding: 40px 6% 40px;
  flex-direction: column;
  gap: 50px;
  animation-name: spawn;
  animation-duration: .6s;
  animation-iteration-count: 1;
  animation-timing-function: ease-in-out;
}
.header-text {
  gap: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 50px;
  width: 100%;
  margin: 0 auto;
}
.header-text h1 {
  position: relative;
  font-size: calc(2rem + 2vw);
  font-family: 'Lora';
  font-weight: 900;
  animation: text-background 20s ease infinite;
  background: linear-gradient(50deg, var(--verde), #141414, var(--verde), #141414 ,var(--verde));
  background-clip: text;
  color: transparent;
  background-size: 200% 200%;
}
@keyframes text-background {
  0%{
    background-position: 0% 50%;
  }
  50%{
    background-position: 100% 50%;
  }
  100%{
    background-position: 0% 50%;
  }
}
.header-text-container p {
  width: 60%;
  font-size: calc(0.8rem + 1vw);
  font-weight: 500;
  font-family: 'Rubik';
  color: #141414;
}
.header-button-container {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: space-between;
}
.header-button {
  font-size: calc(0.8rem + 0.5vw);
  text-decoration: none;
  font-family: 'Rubik';
  font-weight: 500;
  padding: 20px;
  color: var(--verde);
  background-color: #141414;
  transition: 0.2s ease;
  border: 2px solid #141414;
}
.header-button:hover {
  color: #141414;
  background-color: var(--verde);
}
.flechita-header-button {
  position: relative;
  top: 1px;
  scale: 2;
  margin-left: -12px;
  transition: 0.2s ease;
  opacity: 0;
}
.header-button:hover .flechita-header-button {
  scale: 1.7;
  margin-left: 5px;
  opacity: 1;
}
@keyframes spawn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@media (max-width: 1000px){
  header{
    height: 90vw;
  }
}
@media (max-width: 700px){
  header{
    height: 600px;
  }
}
@media (max-width: 500px) {
  .header-text-container{
  gap: 20px;
}
  .header-button-container {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: space-between;
  flex-direction: column;
  gap: 20px;
}
.header-text-container p {
  align-self: flex-start;
  width: 100%;
}
.header-button {
  font-size: calc(0.8rem + 0.5vw);
  text-decoration: none;
  font-family: 'Rubik';
  font-weight: 500;
  padding: 20px;
  color: var(--verde);
  background-color: #141414;
  transition: 0.2s ease;
  border: 2px solid #141414;
  align-self: flex-end;
}
.header-button:hover {
  color: #141414;
  background-color: var(--verde);
}
}
</style>

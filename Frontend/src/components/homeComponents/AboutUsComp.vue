<template>
  <section>
    <div class="text-container">
      <h2>DE LA MANO DE LOS CREADORES</h2>
      <h1>Sobre Leafy</h1>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ex cupiditate, dicta, tempora, ipsa ducimus molestias laborum optio omnis rem iste odio at laboriosam repellendus rerum! Cupiditate quis minima alias.
      </p>
      <RouterLink class="info-button"
          >MÁS INFORMACIÓN
          <span
            ><svg
              class="flechita-info-button"
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
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
section {
  background-image: url('../../assets/images/about.jpg');
  background-position: center;
  background-size: cover;
  width: 100%;
  padding: 9% 0;
}
.text-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 100%;
  padding: 50px 8%;
  background-color: rgba(153, 153, 153, 0.486);
  color: #141414;
}
h2 {
  font-family: 'Rubik';
  font-size: calc(1rem + .7vw);
  font-weight: 500;
}
h1{
  font-family: 'Lora';
  font-size: calc(2rem + 2vw);
}
p{
  font-family: 'Rubik';
  font-size: calc(.8rem + .7vw);
}
.info-button {
  margin-top: 50px;
  width: max-content;
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
.info-button:focus{
  outline: none;
}
.info-button:hover {
  color: #141414;
  background-color: var(--verde);
}
.flechita-info-button {
  position: relative;
  top: 1px;
  scale: 2;
  margin-left: -12px;
  transition: 0.2s ease;
  opacity: 0;
}
.info-button:hover .flechita-info-button {
  scale: 1.7;
  margin-left: 5px;
  opacity: 1;
}
</style>

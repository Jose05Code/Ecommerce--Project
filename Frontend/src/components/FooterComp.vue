<template>
  <footer>
    <section class="footer-mobile">
      <div @click="active1" class="desplegar tienda">
        <h2>qheuqhdiajdioand</h2>
        <div class="svg plus" :class="{ rotate: isActive1 }">
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_4112_32851)">
              <path d="M3.125 10.5H16.875" stroke="#B3B3B3" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
              <path d="M10 3.625V17.375" stroke="#B3B3B3" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
            </g>
            <defs>
              <clipPath id="clip0_4112_32851">
                <rect width="20" height="20" fill="white" transform="translate(0 0.5)" />
              </clipPath>
            </defs>
          </svg>
        </div>
      </div>
      <transition name="despliegue">
        <div v-if="isActive1" class="desplegable">
          <p>
            ahdkjahdak hakljdhawkjdha dahaiuahaj hakawfgakfjsfgskjfgfai hfaiwf hifha fuehasf iuhf
          </p>
        </div>
      </transition>

      <div @click="active2" class="desplegar servicio">
        <h2>awdafafawf ag</h2>
        <div class="svg plus" :class="{ rotate: isActive2 }">
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_4112_32851)">
              <path d="M3.125 10.5H16.875" stroke="#B3B3B3" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
              <path d="M10 3.625V17.375" stroke="#B3B3B3" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
            </g>
            <defs>
              <clipPath id="clip0_4112_32851">
                <rect width="20" height="20" fill="white" transform="translate(0 0.5)" />
              </clipPath>
            </defs>
          </svg>
        </div>
      </div>
      <transition name="despliegue">
        <div v-if="isActive2" class="desplegable">
          <p>
            andanw doiHAWdi hadoihawodihaoidhqw89dy891984 hdkajsdoiaJHSoidadoiajskcns knadhaoshd
          </p>
        </div>
      </transition>
      <div @click="active3" class="desplegar contactenos">
        <h2>aefsaefsef hrhadg af</h2>
        <div class="svg plus" :class="{ rotate: isActive3 }">
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_4112_32851)">
              <path d="M3.125 10.5H16.875" stroke="#B3B3B3" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
              <path d="M10 3.625V17.375" stroke="#B3B3B3" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
            </g>
            <defs>
              <clipPath id="clip0_4112_32851">
                <rect width="20" height="20" fill="white" transform="translate(0 0.5)" />
              </clipPath>
            </defs>
          </svg>
        </div>
      </div>
      <transition name="despliegue">
        <div v-if="isActive3" class="desplegable">
          <p>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laudantium, dignissimos amet
            consequatur consectetur sit assumenda eius alias non doloribus, enim deserunt, fuga
            veritatis dolore quidem reprehenderit sed iusto sapiente iste.
          </p>
        </div>
      </transition>
    </section>
    <section class="footer-desktop">
      <div>
        <div class="logo">
          <img class="logo-img" src="../assets/images/logo.png" alt="logo" />
          <img class="logo-img-text" src="../assets/images/text_logo.png" alt="logo" />
        </div>
      </div>
      <div class="footer-text">
        <h2>Tienda</h2>
        <p>Catalogo</p>
        <p>Articulos individuales</p>
        <p>Colecciones Linos</p>
        <p>Talleres Linos</p>
      </div>
      <div class="footer-text">
        <h2>Contactenos</h2>
        <p>+53 53093529</p>
        <p>linosPottery@gmail.com</p>
        <p>Artesano Laboratorio 28 # 4505 e/ 45 y 47. Playa. Habana. Cuba</p>
      </div>

      <div class="footer-text">
        <h2>Servicio al cliente</h2>
        <p>Sobre nosotros</p>
        <p>Preguntas frecuentes</p>
        <p>Registro</p>
      </div>
    </section>
    <div class="social">
      <h2>SÍGUENOS</h2>
      <div class="redes">
        <a class="sociales" href=""><svg class="sociales-svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <path
              d="M17.2137 13.3297L17.8356 9.23457H13.9452V6.57826C13.9452 5.45763 14.4877 4.36467 16.2301 4.36467H18V0.878262C18 0.878262 16.3945 0.601562 14.8603 0.601562C11.6548 0.601562 9.56164 2.56336 9.56164 6.11341V9.23457H6V13.3297H9.56164V23.23C10.2767 23.3435 11.0082 23.4016 11.7534 23.4016C12.4986 23.4016 13.2301 23.3435 13.9452 23.23V13.3297H17.2137Z"
              fill="#999999" />
          </svg></a>

        <a class="sociales" href=""><svg class="sociales-svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_4112_32856)">
              <path
                d="M12 2.16276C15.206 2.16276 15.5824 2.17705 16.8496 2.23422C18.0215 2.28662 18.655 2.48194 19.079 2.64867C19.6411 2.8678 20.0413 3.12505 20.4605 3.54426C20.8797 3.96348 21.1417 4.36364 21.3561 4.92576C21.5181 5.34974 21.7182 5.98333 21.7706 7.15522C21.8277 8.42239 21.842 8.79873 21.842 12.0048C21.842 15.2108 21.8277 15.5871 21.7706 16.8543C21.7182 18.0262 21.5228 18.6598 21.3561 19.0838C21.137 19.6459 20.8797 20.046 20.4605 20.4653C20.0413 20.8845 19.6411 21.1465 19.079 21.3609C18.655 21.5228 18.0215 21.7229 16.8496 21.7753C15.5824 21.8325 15.206 21.8468 12 21.8468C8.79397 21.8468 8.41763 21.8325 7.15046 21.7753C5.97857 21.7229 5.34498 21.5276 4.921 21.3609C4.35888 21.1417 3.95872 20.8845 3.5395 20.4653C3.12029 20.046 2.85828 19.6459 2.64391 19.0838C2.48194 18.6598 2.28186 18.0262 2.22946 16.8543C2.17229 15.5871 2.158 15.2108 2.158 12.0048C2.158 8.79873 2.17229 8.42239 2.22946 7.15522C2.28186 5.98333 2.47718 5.34974 2.64391 4.92576C2.86304 4.36364 3.12029 3.96348 3.5395 3.54426C3.95872 3.12505 4.35888 2.86304 4.921 2.64867C5.34498 2.4867 5.97857 2.28662 7.15046 2.23422C8.41763 2.17229 8.79874 2.16276 12 2.16276ZM12 0C8.74157 0 8.33188 0.0142914 7.05042 0.0714569C5.77372 0.128622 4.90195 0.333466 4.13974 0.628821C3.34895 0.933704 2.68202 1.34815 2.01509 2.01509C1.34815 2.68202 0.938468 3.35371 0.628821 4.13974C0.333466 4.90195 0.128623 5.77372 0.071457 7.05518C0.0142914 8.33188 0 8.74156 0 12C0 15.2584 0.0142914 15.6681 0.071457 16.9496C0.128623 18.2263 0.333466 19.0981 0.628821 19.865C0.933704 20.6558 1.34815 21.3227 2.01509 21.9897C2.68202 22.6566 3.35371 23.0663 4.13974 23.3759C4.90195 23.6713 5.77372 23.8761 7.05519 23.9333C8.33665 23.9905 8.74157 24.0048 12.0048 24.0048C15.268 24.0048 15.6729 23.9905 16.9544 23.9333C18.2311 23.8761 19.1028 23.6713 19.8698 23.3759C20.6606 23.0711 21.3275 22.6566 21.9945 21.9897C22.6614 21.3227 23.0711 20.6511 23.3807 19.865C23.6761 19.1028 23.8809 18.231 23.9381 16.9496C23.9953 15.6681 24.0095 15.2632 24.0095 12C24.0095 8.7368 23.9953 8.33188 23.9381 7.05042C23.8809 5.77372 23.6761 4.90195 23.3807 4.13497C23.0758 3.34418 22.6614 2.67725 21.9945 2.01032C21.3275 1.34339 20.6558 0.933704 19.8698 0.624057C19.1076 0.328702 18.2358 0.123859 16.9544 0.0666931C15.6681 0.0142914 15.2584 0 12 0Z"
                fill="#999999" />
              <path
                d="M12.0003 5.83984C8.59894 5.83984 5.83594 8.59808 5.83594 12.0042C5.83594 15.4103 8.59417 18.1685 12.0003 18.1685C15.4064 18.1685 18.1646 15.4103 18.1646 12.0042C18.1646 8.59808 15.4064 5.83984 12.0003 5.83984ZM12.0003 16.001C9.78989 16.001 7.9987 14.2098 7.9987 11.9994C7.9987 9.78903 9.78989 7.99784 12.0003 7.99784C14.2107 7.99784 16.0019 9.78903 16.0019 11.9994C16.0019 14.2098 14.2107 16.001 12.0003 16.001Z"
                fill="#999999" />
              <path
                d="M18.4074 7.02968C19.202 7.02968 19.8461 6.38556 19.8461 5.59101C19.8461 4.79646 19.202 4.15234 18.4074 4.15234C17.6129 4.15234 16.9688 4.79646 16.9688 5.59101C16.9688 6.38556 17.6129 7.02968 18.4074 7.02968Z"
                fill="#999999" />
            </g>
            <defs>
              <clipPath id="clip0_4112_32856">
                <rect width="24" height="24" fill="white" />
              </clipPath>
            </defs>
          </svg></a>
        <a class="sociales" href=""><svg class="sociales-svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <path
              d="M21.0586 7.17919C21.0678 7.39039 21.0679 7.59199 21.0679 7.80319C21.0771 14.2064 16.3726 21.5984 7.76939 21.5984C5.23194 21.5984 2.7408 20.84 0.601562 19.4192C0.971993 19.4672 1.34242 19.4864 1.71285 19.4864C3.81505 19.4864 5.86168 18.7568 7.51935 17.4032C5.51903 17.3648 3.75948 16.0112 3.14827 14.0336C3.85209 14.1776 4.57443 14.1488 5.25973 13.9472C3.08345 13.5056 1.51838 11.5184 1.50912 9.2048C1.50912 9.1856 1.50912 9.1664 1.50912 9.1472C2.15737 9.5216 2.88897 9.7328 3.62983 9.752C1.5832 8.3312 0.944211 5.49919 2.18515 3.28158C4.56517 6.31519 8.06574 8.14879 11.8256 8.3504C11.4459 6.67039 11.9645 4.90398 13.1777 3.71358C15.0576 1.87997 18.0211 1.97597 19.7991 3.92478C20.8456 3.71358 21.855 3.31038 22.7718 2.74398C22.4199 3.86718 21.6883 4.81758 20.7159 5.42239C21.642 5.30719 22.5496 5.04798 23.4016 4.66398C22.7718 5.64319 21.9754 6.48799 21.0586 7.17919Z"
              fill="#999999" />
          </svg></a>
      </div>
      <p>Linos. 2024 Tienda de cerámica.</p>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'

let isActive1 = ref(false)

let isActive2 = ref(false)

let isActive3 = ref(false)

const active1 = () => {
  isActive1.value = !isActive1.value
}
const active2 = () => {
  isActive2.value = !isActive2.value
}
const active3 = () => {
  isActive3.value = !isActive3.value
}
</script>

<style scoped>
footer {
  transform: translateY(60px);
  padding: 40px 25px;
  background-color: #2a2a2a;
}

/* ====================ESTILOS DE LA VISTA MOBILE==================== */
/* ==========Estilos del menu desplecable========== */
.desplegar {
  transition: 0.2s ease;
  position: relative;
  z-index: 5;
  background-color: #2a2a2a;
  display: flex;
  justify-content: space-between;
  padding: 25px 0;
  border-bottom: 2px solid #525252;
  font-size: 12px;
  align-items: center;
  cursor: pointer;
}

.desplegable {
  position: relative;
  z-index: 1;
  padding: 40px 0;
}

/* ==========Estilos de los SVG========== */
.svg {
  transition: 0.2s ease;
}

.desplegar:hover svg path,
.desplegar:hover h2,
.desplegar:hover {
  stroke: #42aa25;
  color: #42aa25;
  border-bottom-color: #42aa25;
}

.rotate {
  transform: rotate(45deg);
}

.sociales:hover .sociales-svg path {
  fill: #42aa25;
}

.plus {
  scale: 1;
}

/* ==========Estilos de los <transition/>========== */

.despliegue-enter-active,
.despliegue-leave-active {
  transition: 0.2s ease;
}

.despliegue-enter-from,
.despliegue-leave-to {
  padding: 0;
  opacity: 0;
  height: 0;
}

/* ==========Estilos de los textos========== */

h2 {
  font-size: calc(12px + 0.5vw);
  font-weight: 400;
  color: #b3b3b3;
}

p {
  font-family: 'Rubik';
  font-size: calc(8px + 0.5vw);
  color: #e5e5e5;
  line-height: 16px;
}

h2,
svg path {
  transition: 0.2s ease;
}


/* ====================ESTILOS DE LA VISTA DESKTOP==================== */

.footer-desktop {
  display: none;
  justify-content: space-between;
  padding: 60px 3% 0 3%;
  gap: 70px;
}

.logo {
  flex-grow: 1;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.logo img {
  height: min-content;
}

.logo-img-text {
  width: 120px;
}

.logo-img {
  width: 80px;
}

.footer-text {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* ==========Estilos de las redes sociales========== */
.social {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  max-width: 350px;
  margin: 0 auto;
  margin-top: 50px;
}

.redes {
  display: flex;
  gap: 20px;
}

/* ====================MEDIA QUERYS==================== */
@media (min-width: 1000px) {
  .footer-desktop {
    display: flex;
  }

  .footer-mobile {
    display: none;
  }
}

@media (min-width: 1400px) {
  .logo-img-text {
    width: 160px;
  }

  .logo-img {
    width: 120px;
  }
}
</style>

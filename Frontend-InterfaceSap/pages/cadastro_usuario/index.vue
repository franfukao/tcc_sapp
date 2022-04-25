// Cadastro Usuario
<template>
  <div class="cont">
    <headers />
    <div class="principal">
      <form class="base" method="POST">
        <h1>Cadastro Usuario</h1>
        <input
          type="text"
          name="idUserFK"
          class="inputs"
          id="idUserFK"
          placeholder="Nome"
          v-model="cadastro.username"
          required
        />
        <input
          type="email"
          name="email"
          class="inputs"
          id="input3"
          placeholder="email"
          v-model="cadastro.email"
          required
        />
        <input
          type="number"
          name="edv"
          class="inputs"
          id="input4"
          placeholder="EDV"
          v-model="cadastro.edv"
          required
        />
        <input
          type="text"
          name="responsavel"
          class="inputs"
          id="input4"
          placeholder="Responsavel"
          v-model="cadastro.edv"
          required
        />
        <select name="nivelAcesso" class="inputs">
          <option value="adm">Administrador</option>
          <option value="apre">Aprendiz</option>
        </select>

        <input
          type="password"
          name="senha"
          class="inputs"
          id="input5"
          placeholder="Senha"
          v-model="cadastro.password"
          required
        />
        <button type="submit" @click="fetchCadastro">Enviar</button>
      </form>
    </div>
    <footers />
  </div>
</template>

<script>
import headers from '../../components/headers.vue'
export default {
  components: { headers },
  name: 'home',
  data() {
    return {
      cadastro: {
        username: '',
        password: '',
        email: '',
        edv: '',
        idRespFK: 1,
        idNivelAcessFK: 1,
      },
    }
  },

  methods: {
    fetchCadastro: async function () {
      let obj = this.cadastro
      let send = true
      console.log(1)
      for (const [key, value] of Object.entries(this.cadastro)) {
        if (document.getElementById(key)) {
          if (value == '') {
            send = false
            document.getElementById(key).style.borderColor = ''
          } else {
            document.getElementById(key).style.borderColor = '#E5E5E5'
          }
        }
      }

      if (send) {
        await this.$axios
          .$post(
            'http://localhost:8000/logonview/',
            JSON.stringify([this.cadastro]),
            {
              headers: {
                'Content-Type': 'application/json',
              },
            }
          )
          .then((response) => {
            console.log(response)
            alert('usuario cadastrado!')
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/cadastro_usuario/cadastro_usuario.scss';
</style>

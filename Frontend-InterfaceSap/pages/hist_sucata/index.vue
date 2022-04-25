<template>
  <div class="cont">
    <div class="page">
      <div class="base">
        <div class="titulo">
          <h1>Historico de Sucata</h1>
          <hr />
        </div>
        <div class="cards">
          <div class="card-one c">
            <h1>Cod Sucata</h1>
            <h4>Descrição</h4>
            <h4>Texto</h4>
            <h4>Data</h4>
            <NuxtLink class="btn-ir" to="#">Add foto</NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'hist_produto',
  layout: 'standard',
  middleware: 'auth',
}
</script>

<style lang="scss" scoped>
@import '@/pages/hist_produto/hist_produto.scss';
</style>

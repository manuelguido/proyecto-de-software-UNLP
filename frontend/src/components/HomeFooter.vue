<template>
  <!-- Footer -->
  <mdb-footer id="footer">
    <div class="footer-copyright text-center py-3">
      <mdb-container fluid>
        <mdb-row class="px-lg-5 px-md-4 justify-content-center">
          <mdb-col lg="6" class="text-left">
            <p class="my-0 py-0">© 2020 <router-link to="/">Orquesta Escuela Berisso</router-link> Todos los derechos reservados.</p>
          </mdb-col>
        </mdb-row>
      </mdb-container>
    </div>
  </mdb-footer>
  <!-- Footer -->
</template>

<script>
import { mdbFooter, mdbContainer, mdbRow, mdbCol } from 'mdbvue'
export default {
  name: 'FooterPage',
  components: {
    mdbFooter,
    mdbContainer,
    mdbRow,
    mdbCol
  }
}
</script>

<style scoped>
#footer {
  margin: 0 !important;
}
.footer-copyright {
  width: 100vw !important;
  background: #0A0924 !important;
}
@media (min-width: 992px) {
  .footer-copyright {
    height: 50px;
  }
}
.footer-copyright p {
  color: var(--white-a);
  font-size: 13px;
  font-weight: 600;
}
.footer-copyright a {
  color: var(--seed-link);
}
.footer-copyright a:hover,
.footer-copyright a:active {
  color: var(--seed-link-dark);
}
</style>

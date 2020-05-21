<template>
<div>
  <!-- Contenido Principal -->
    <main class="panel">
      <!-- Row-->
      <div class="row m-0 p-0">
        <!-- Menu-->
        <aside id="panel-menu" class="p-0 uns mobile-hide">
          <div id="panel-menu-inner" class="p-0 panel-menu navbar-light">
            <ul class="list-group list-group-flush">
              <li class="list-group-item menuItem" role="button"><a href="/panel_estudiantes"><i class="fas fa-user-graduate mr-2"></i>Estudiantes</a></li>
              <li class="list-group-item menuItem" role="button"><a href="/panel_docentes"><i class="fas fa-user-friends mr-2"></i>Docentes</a></li>
            </ul>
            <hr>
            <ul class="list-group list-group-flush">
              <li class="list-group-item menuItem mt-auto" role="button"><a href="/logout"><i class="fas fa-sign-out-alt black5 mr-2 my-0"></i>Salir</a>
            </ul>
          </div>
        </aside>
        <!-- /.Menu -->

        <!-- Columna full width -->
        <div id="panel-content" class="col p-0">
          <div class="container-fluid w-100 m-0 panel-banner">
            <div class="row">
              <div class="col-12 py-4 px-5 my-lg-2">
                <h1 class="h4-responsive w600 ls02 m-0" id="panel-title"></h1>
              </div>
            </div>
          </div>

          <!-- Container Fluid -->
          <div class="container-fluid w-100 p-4 m-0">

          </div>
          <!-- /.Container Fluid -->
        </div>
      <!--/.Columna full width -->
    </div>
    <!-- /.Row-->
  </main>
  <!-- /Main -->
</div>
</template>

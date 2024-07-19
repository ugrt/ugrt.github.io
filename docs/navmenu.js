document.write(`
  <nav class="sticky-nav">
      <a href="index.html">
          <img id="no-background-team-logo" src="images/Logo_noBgd.png" />
      </a>

      <ul class="nav-list"> <!-- This is the list of the different pages-->
          <!-- <li><a href="index.html">Home</a></li> (original home button) -->
          <li><a href="about-us.html">About Us</a></li>
          <li><a href="projects-grid.html">Projects</a>
              <ul id="projects-dropdown">
                  <li><a href="index.html"></a>Mechanical</a></li>
                  <li><a href="index.html"></a>Electrical</a></li>
                  <li><a href="index.html"></a>Software</a></li>
                  <li><a href="index.html"></a>Firmware</a></li>
                  <li><a href="index.html"></a>Other</a></li>
              </ul>
          </li>
          <li><a href="index.html">Sponsors</a></li>
          <li><a href="index.html">Contact Us</a></li>
      </ul>
  </nav>
`);
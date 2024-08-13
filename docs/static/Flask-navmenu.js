document.write(`
    <nav class="sticky-nav">
        <a href="index.html">
            <img id="no-background-team-logo" src="styles/Logo_noBgd.png" />
        </a>

        <ul class="nav-list"> <!-- This is the list of the different pages-->
            <!-- <li><a href="/">Home</a></li> (original home button) -->
            <li><a href="/">About Us</a></li>
            <li><a href="/projects">Projects</a>
                <ul id="projects-dropdown">
                    <li><a href="/projects/mechanical"></a>Mechanical</a></li>
                    <li><a href="/projects/electrical"></a>Electrical</a></li>
                    <li><a href="/projects/programming"></a>Software</a></li>
                    <li><a href="/"></a>Firmware</a></li>
                    <li><a href="/"></a>Other</a></li>
                </ul>
            </li>
            <li><a href="/">Sponsors</a></li>
            <li><a href="/">Contact Us</a></li>
        </ul>
    </nav>
`);
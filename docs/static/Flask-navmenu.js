document.write(`
    <nav class="sticky-nav">
        <a href="/">
            <img id="no-background-team-logo" src="{{url_for('static',filename='images\\StellaDoingElectricalThings.jpg')}}">
        </a>

        <ul class="nav-list"> <!-- This is the list of the different pages-->
            <!-- <li><a href="/">Home</a></li> (original home button) -->

            <div class="dropdown">
                <li><a href="/about-us">About Us</a></li>

                <!--
                <div class="dropdown-content">
                    <a href="/">Opportunities</a>
                </div>
                -->
                
            </div>

            <div class="dropdown">
                <li><a href="/projects">Projects</a></li>
                <div class="dropdown-content">
                    <a href="/projects/electrical">Electrical</a>
                    <a href="/projects/mechanical">Mechanical</a>
                    <a href="/projects/programming">Programming</a>
                    <a href="/projects/marketing">Marketing</a>
                </div>
            </div>

            <div class="dropdown">
                <li><a href="/">Sponsorships</a></li>
                <div class="dropdown-content">
                    <a href="/">Opportunities</a>
                </div>
            </div>

            <div class="dropdown">
                <li><a href="/">Contact Us</a></li>

                <!--
                <div class="dropdown-content">
                    <a href="/">Opportunities</a>
                </div>
                -->

            </div>
        </ul>
    </nav>
`);
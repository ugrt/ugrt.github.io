
document.write(`
    <nav class="sticky-nav">
        <a href="/">
            <img id="no-background-team-logo" src="\\static\\images\\Logo_noBgd.png">
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
                <li><a href="/subteams">Subteams</a></li>
                <div class="dropdown-content">
                    <a href="/subteams/electrical">Electrical</a>
                    <a href="/subteams/mechanical">Mechanical</a>
                    <a href="/subteams/programming">Programming</a>
                    <a href="/subteams/marketing">Marketing</a>
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
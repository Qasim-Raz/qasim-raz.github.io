import codecs

lines = open('e:/portfolio/index.html', encoding='utf-8').read().splitlines()
start_num = 124 # line 125 is index 124
end_num = 319 # line 319 is index 318

new_lines = """                        <!-- 1. About and Profile Pic Side by Side -->
                        <div class="row mb-5">
                            <div class="col-md-8 order-2 order-md-1">
                                <div class="about-me">
                                    <div class="title-box-2 mb-4">
                                        <h5 class="title-left">
                                            About me
                                        </h5>
                                    </div>
                                    <p style="text-align: justify;" class="lead">
                                        Results-driven Full Stack Web Developer with strong experience in Vue.js, PHP,
                                        and Laravel. Proven ability to design, develop, and maintain scalable web
                                        applications with clean architecture. Highly adaptable, detail-oriented, and
                                        passionate about continuous learning and performance optimization.
                                    </p>
                                    
                                    <div class="about-info mt-4">
                                        <div class="row">
                                            <div class="col-sm-6">
                                                <p><span class="title-s">Name: </span> <span>Qasim Raza</span></p>
                                                <p><span class="title-s">Profile: </span> <span>Full Stack Web Developer</span></p>
                                            </div>
                                            <div class="col-sm-6">
                                                <p><span class="title-s">Email: </span> <a href="mailto:qasim.raza293742@gmail.com">qasim.raza293742@gmail.com</a></p>
                                                <p><span class="title-s">Phone: </span> <a class="text-primary callNow_CTA" href="tel:+923022937918">(+92) 302 2937918</a></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-4 order-1 order-md-2 mb-4 mb-md-0 d-flex align-items-center justify-content-center">
                                <div class="about-img cursor-pointer zoom-on-hover px-4">
                                    <img src="img/ProfillePic1.jpeg" class="img-fluid rounded b-shadow-a w-100" alt="Qasim Raza">
                                </div>
                            </div>
                        </div>

                        <!-- 2. Skills -->
                        <div class="row mb-5 pb-4 border-bottom">
                            <div class="col-md-12">
                                <div class="title-box-2 mb-4">
                                    <h5 class="title-left">Skills</h5>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="skill-mf">
                                    <div class="zoom-on-hover">
                                        <span>HTML/CSS/Bootstrap</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>JavaScript (ES6+)</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>Vue.js</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>Vuetify</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>Vuex</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>Responsive UI</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>jQuery</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="skill-mf">
                                    <div class="zoom-on-hover">
                                        <span>PHP</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>Laravel</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>MySQL</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>Git</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>REST APIs</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="zoom-on-hover">
                                        <span>OOP & C++ Basics</span> <span class="pull-right">100%</span>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 3. Experience section -->
                        <div class="row mb-5 pb-4 border-bottom">
                            <div class="col-md-12">
                                <div class="title-box-2 mb-4">
                                    <h5 class="title-left">Experience</h5>
                                </div>
                                
                                <div class="resume-item mb-4">
                                    <p style="text-align: justify;" class="mb-2"><b>Web Developer — Shayan Pakistan (Sep 2025 – Dec 2025)</b></p>
                                    <ul style="text-align: justify;">
                                        <li>Lead backend development using PHP and Laravel</li>
                                        <li>Design scalable database architecture and APIs</li>
                                        <li>Improve system performance and maintain code quality</li>
                                    </ul>
                                </div>
                                
                                <div class="resume-item mb-4">
                                    <p style="text-align: justify;" class="mb-2"><b>Front-End Developer — WindshieldHub (Apr 2025 – Sep 2025)</b></p>
                                    <ul style="text-align: justify;">
                                        <li>Developed and maintained complex, responsive UI components using Vue.js and Bootstrap, ensuring cross-browser compatibility and optimal performance.</li>
                                        <li>Collaborated closely with UI/UX designers to translate wireframes into high-quality code and partnered with QA teams to identify and resolve critical front-end bugs.</li>
                                        <li>Optimized application speed and scalability by refactoring legacy code and improving component reusability.</li>
                                    </ul>
                                </div>
                                
                                <div class="resume-item mb-4">
                                    <p style="text-align: justify;" class="mb-2"><b>Front-End Developer Intern — WindshieldHub (Dec 2024 – Apr 2025)</b></p>
                                    <ul style="text-align: justify;">
                                        <li>Assisted in building responsive web interfaces using Vue.js, focusing on creating clean and maintainable CSS with Bootstrap.</li>
                                        <li>Implemented Vuex for centralized state management, improving data flow and consistency across multiple application modules.</li>
                                        <li>Participated in code reviews and agile ceremonies, gaining hands-on experience in a professional software development lifecycle</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <!-- 4. Education and Certifications Side by Side -->
                        <div class="row">
                            <div class="col-md-6 mb-4 mb-md-0">
                                <div class="title-box-2 mb-4">
                                    <h5 class="title-left">Education</h5>
                                </div>
                                <ul>
                                    <li class="mb-3" style="text-align: justify;"><b>Associate Degree in Web Design & Development</b><br>Virtual University of Pakistan (2024 – 2026)</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <div class="title-box-2 mb-4">
                                    <h5 class="title-left">Certifications</h5>
                                </div>
                                <ul>
                                    <li class="mb-3"><b>Laravel Certification</b><br>(Udemy, Piotr Jura) — ongoing (2025)</li>
                                    <li class="mb-3"><b>Vue.js Course</b><br>(Udemy, Stephen Grider) — 2024</li>
                                    <li class="mb-3"><b>C++ Essentials 1</b><br>(Cisco NetAcad) — Dec 2024</li>
                                </ul>
                            </div>
                        </div>"""

final_lines = lines[:124] + [new_lines] + lines[319:]
with codecs.open('e:/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(final_lines))
print("Done!")

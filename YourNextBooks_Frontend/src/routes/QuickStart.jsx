import React, { useEffect } from "react";
import MainFooter from '../components/MainFooter';

export default function QuickStart() {
	const openModalBtnRef = React.useRef(null)
	useEffect(() => {
		if (openModalBtnRef.current) {
			openModalBtnRef.current.click()
		}
	})

	return (
		<>
			<header className="vw-100 p-3 d-flex justify-content-between justify-content-md-around">
				<a href="/" target="_self" className="fs-3 text-none link-offset-3 fw-bold">Your Next Books</a>
				<button ref={openModalBtnRef} id="open-modal-description" className="btn btn-primary rounded-circle" data-bs-toggle="modal" data-bs-target="#description-modal">?</button>
			</header>
			<main className="vh-100 text-center d-flex flex-column justify-content-center px-2 container-sm px-md-5">
				<h1>Olá, seja bem vindo!</h1>
				<p>Vamos descubrir quais são os melhores livros para você ler baseado nas suas respostas a questões triviais que faremos para você e com a integração com  API oficial da Amazon!</p>
				<a href="/questões" className="btn btn-link bg-success text-light text-decoration-none fw-bold">Bora começar!</a>
			</main>
			<div className="modal" tabindex="-1" id="description-modal">
				<div className="modal-dialog">
					<div className="modal-content">
						<div className="modal-header">
							<h5 className="modal-title text-danger text-uppercase fw-bold">AVISO RÁPIDO!</h5>
							<button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
						</div>
						<div className="modal-body">
							<p>Este projeto de portfólio freelancer não tem foco em design ou ferramentas de frontend, por isso mantenho nele o design padrão do Bootstrap, porém ele tem um foco de demonstrar minhas habilidades em automação como integração com APIs e envio de emails.<br />Foram usadas as seguintes tecnologias no projeto:<br /></p>
							<ol>
								<li>
									<span>FRONTEND:</span>
									<ul>
										<li>HTML (Linguagem de marcação)</li>
										<li>JAVASCRIPT (Linguagem de programação)</li>
										<li>BOOTSTRAP (Framework CSS & JAVASCRIPT)</li>
										<li>REACT (Framework JAVASCRIPT)</li>
									</ul>
								</li>
								<li>
									<span>BACKEND:</span>
									<ul>
										<li>PYTHON (Linguagem de programação)</li>
										<li>REQUESTS (Bíblioteca do Python)</li>
										<li>FLASK (Framework do Python)</li>
										<li>SMTPLIB (Bíblioteca do Python)</li>
									</ul>
								</li>
							</ol>
						</div>
					</div>
				</div>
			</div>
			<MainFooter />
		</>
	)
}

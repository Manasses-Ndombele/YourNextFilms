import MainFooter from '../components/MainFooter';

export default function Questions() {
	return (
		<>
			<main className="vh-100 text-center d-flex flex-column justify-content-center p-2 mb-3 container-sm px-md-5">
				<h1>Parabéns, FULANO!</h1>
				<p>Já temos dados suficientes para te sugerir 3 livros da Amazon coletados através da API, verifique o email que enviamos para: emaildofulano@servicodeemail.com</p>
				<p>Se o email ainda não caiu espere um pouco e depois verifique também na caixa de SPAM ou no Lixo.</p>
			</main>
			<MainFooter />
		</>
	)
}

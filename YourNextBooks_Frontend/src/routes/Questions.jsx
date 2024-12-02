import axios from "axios";
import { useState, useEffect } from "react";
import MainFooter from '../components/MainFooter';

export default function Questions() {
	const [emailField, setEmailField] = useState("")
	const [nameField, setNameField] = useState("")
	const [categoryField, setCategoryField] = useState("")
	const [firstBookField, setFirstBookField] = useState("")
	const [secondBookField, setSecondBookField] = useState("")

	const handleSubmit = async (e) => {
		e.preventDefault()
		const formData = {
		  name: nameField,
		  email: emailField,
		  category: categoryField,
		  firstBook: firstBookField,
		  secondBook: secondBookField
		}

		try {
		  const response = await axios.post('http://127.0.0.1:5000/api/user-datas', formData)
		  console.log(response.data)
		  alert('Formulário enviado com sucesso!')
		} catch (error) {
		  console.error('Erro ao enviar o formulário:', error)
		  alert('Ocorreu um erro ao enviar o formulário.')
		}
	}

	return (
		<>
			<main className="text-center d-flex flex-column justify-content-center p-2 mb-3 container-sm px-md-5">
				<h1>Responda as questões abaixo e em seguida vamos te enviar um email com os resultados da análise computacional!</h1>
				<p>Os seus dados não serão salvos mas serão apenas partilhados com a Amazon pois servirão de base para as recomendações que enviaremos no seu email.</p>
				<form onSubmit={handleSubmit}>
					<label htmlFor="email-field" className="form-label">Informe seu email</label>
					<input type="email" id="email-field" className="form-control" placeholder="Email" value={emailField} onChange={(e) => setEmailField(e.target.value)} required />
					<br />
					<label htmlFor="name-field" className="form-label">Informe seu nome</label>
					<input type="text" id="name-field" className="form-control" placeholder="Nome" value={nameField} onChange={(e) => setNameField(e.target.value)} required />
					<br />
					<label htmlFor="category-field" className="form-label">Qual categoria de livros você gosta?</label>
					<select className="form-select" id="category-field" value={categoryField} onChange={(e) => (setCategoryField(e.target.value))} required >
						<option selected disabled value="">Selecione uma categoria</option>
						<option value="Arte e fotografia">Arte e fotografia</option>
						<option value="Dinheiro e negócios">Dinheiro e negócios</option>
						<option value="Cómicos, Mangas e Novelas">Cómicos, Mangas e Novelas</option>
						<option value="Receitas, comidas e vinho">Receitas, comidas e vinho</option>
						<option value="Educação e ensino">Educação e ensino</option>
						<option value="Línguas estrangeiras">Línguas estrangeiras</option>
						<option value="História">História</option>
						<option value="Leis">Leis</option>
						<option value="Literatura e ficção">Literatura e ficção</option>
						<option value="Mistério e suspense">Mistério e suspense</option>
						<option value="Pais e relacionamentos">Pais e relacionamentos</option>
						<option value="Romance">Romance</option>
						<option value="Ciência e Fantasia">Ciência e Fantasia</option>
						<option value="Desporto">Desporto</option>
						<option value="Viagens">Viagens</option>
						<option value="Biografia">Biografia</option>
						<option value="Infantis">Infantis</option>
						<option value="Computação e tecnologia">Computação e tecnologia</option>
						<option value="Hobbies">Hobbies</option>
						<option value="Engenharia">Engenharia</option>
						<option value="Saúde e fitness">Saúde e fitness</option>
						<option value="Política e ciências sociais">Política e ciências sociais</option>
						<option value="Religião e espiritualidade">Religião e espiritualidade</option>
						<option value="Auto-ajuda">Auto-ajuda</option>
					</select>
					<br />
					<label htmlFor="last-reads-fields" className="form-label">Quais foram os títulos das tuas duas últimas leituras?</label>
					<input type="text" id="last-reads-fields" placeholder="Título do primeiro livro" className="form-control" value={firstBookField} onChange={(e) => setFirstBookField(e.target.value)} required />
					<br />
					<input type="text" id="last-reads-fields2" placeholder="Título do segundo livro" className="form-control" value={secondBookField} onChange={(e) => setSecondBookField(e.target.value)} required />
					<br />
					<input type="submit" value="Enviar" className="w-100 btn btn-dark" />
				</form>
			</main>
			<MainFooter />
		</>
	)
}

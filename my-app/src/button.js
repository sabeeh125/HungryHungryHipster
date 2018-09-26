import React from 'react'

const Button = (props) => {
	return (
		<button 
			style={{ backgroundColor : props.color},{margin:props.margin}}

			onClick={props.clickFnc}
		>
			{props.text}
		</button>
		)
}

export default Button;
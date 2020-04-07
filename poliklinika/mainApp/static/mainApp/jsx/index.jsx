class Button extends React.Component{
    constructor (props){
        super(props)
        this.handleClick = this.handleClick.bind(this)
    }
    handleClick(){
        console.log("Hello World!")
    }

    render(){
        return <button onClick={this.handleClick.bind(this)}>Click me!</button>
    }
}

ReactDOM.render(
    <Button />,
    document.getElementById('app')
)
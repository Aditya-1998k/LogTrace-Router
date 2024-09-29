c()
{
	local opts=()
	quote=true docker compose "${opts[@]}" "$@"
	docker compose "${opts[@]}" "$@"
}

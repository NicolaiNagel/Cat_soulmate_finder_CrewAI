# Use an official Python image as a base image
FROM python:3.12-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Install the required dependencies
RUN uv sync --frozen

# Set the command to run the FastAPI app
CMD ["uv", "run", "fastapi", "run", "src/cat_soulmate_finder_crewai", "--port", "8001"]
# Use an official InfluxDB image as the base image
FROM influxdb:latest

# Set the working directory
WORKDIR /etc/influxdb

# Copy the configuration file to the container
COPY influxdb.conf .

# Expose the HTTP and UDP ports
EXPOSE 8086 8091

# Start the InfluxDB service
CMD ["influxd"]
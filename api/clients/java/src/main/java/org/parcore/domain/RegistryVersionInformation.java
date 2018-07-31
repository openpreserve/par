package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModelProperty;

import java.util.Objects;

@SuppressWarnings("unused")
public class RegistryVersionInformation {
    @SerializedName("name")
    private String name = null;

    @SerializedName("registryNamespace")
    private String registryNamespace = null;

    @SerializedName("version")
    private String version = null;

    /**
     * Get name
     * @return name
     **/
    @ApiModelProperty(value = "")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get registryNamespace
     * @return registryNamespace
     **/
    @ApiModelProperty(required = true, value = "")
    public String getRegistryNamespace() {
        return registryNamespace;
    }

    public void setRegistryNamespace(String registryNamespace) {
        this.registryNamespace = registryNamespace;
    }

    /**
     * Get version
     * @return version
     **/
    @ApiModelProperty(required = true, value = "")
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        RegistryVersionInformation registryVersionInformation = (RegistryVersionInformation) o;
        return Objects.equals(this.name, registryVersionInformation.name) &&
                Objects.equals(this.registryNamespace, registryVersionInformation.registryNamespace) &&
                Objects.equals(this.version, registryVersionInformation.version);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, registryNamespace, version);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class RegistryVersionInformation {\n");

        sb.append("    name: ").append(toIndentedString(name)).append("\n");
        sb.append("    registryNamespace: ").append(toIndentedString(registryNamespace)).append("\n");
        sb.append("    version: ").append(toIndentedString(version)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
